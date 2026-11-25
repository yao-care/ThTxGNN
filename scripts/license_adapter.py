"""TH（Thai FDA 公開查詢系統 pertento）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-31）。

2026-10-31：原本的許可證號是程式編造的（見 .claude/th_rebuild_licenses_20261031.py），已改用 pertento 的真實許可證。
pertento 依成分查詢、不用登入（GitHub runner 實測翻頁、詳細資料都可用，run 41148774713；paracetamol 2741 筆約 15 分鐘）；
查詢詞＝證據包 thaifda.query_terms（主名稱＋別名），4 路並行。只更新證據包裡已有許可證的狀態，不新增許可證。
寫回：status＝pertento 原文（คงอยู่／ยกเลิก(日期)／ปลด SMP…），license_status＝valid／cancelled。新資料查不到的許可證保留原狀態。

2026-11-17（用戶要求確認 11-16 排程「新資料查不到」的 2 張）：pertento 的查詢結果連註銷（ยกเลิก）的許可證都列，
所以號碼查不到＝紀錄從系統裡不見了，不是註銷。2A 439/69 (E)（MYOGESIC-G）、2A 440/69 (E)（MYOGESIC-B）：2026-11-17 依成分查
Orphenadrine（294 筆）沒有、詳細頁介面依 newcode 查回傳全部空值；同品名的 2A 6/60 (E)、2A 4/60 (E) 仍是 คงอยู่（證據包本來就有）。
狀態判斷不了，不推定為註銷：
- fetch() 成功（每個查詢詞都翻頁完整）時，把查到的全部許可證號記成 CURRENT（少於 MIN_CURRENT 不判定）。
- preprocess：證據包裡 pertento 來源、不在 CURRENT 的號標 license_status＝unknown（事實層「狀態未知」，不算有效也不算註銷）、
  pertento_not_listed＝第一次發現日，status 改 NOT_LISTED（原值存 status_before_pertento_not_listed）；又出現就還原。
- confirmed_absent(lid)：CURRENT 有資料且號碼不在裡面（＝已確認 pertento 查無此號；狀態未知）。

2026-11-25（第六輪，用戶決定）：RAW_FILE 原本只存 id／status／term，新核准的許可判斷不了是不是本藥。改成：
- 每列另存查詢結果的品名（泰／英）、持有人、法定類別、劑型、newcode（_pertento.search 的原欄位）。
- 成分：查詢結果沒有成分欄，要逐張開詳細資料（_pertento.detail 的 XML_DRUG_FORMULA）。詳細資料存在 FORMULA_FILE
  （{newcode: {fml: [成分原文], status_name, app_date, fetched}}，Release 帶著、每週沿用），只補還沒有的：
  先補「某證據包的查詢詞查得到、但該證據包還沒有」的人用許可（scripts/add_current_licenses.py 補收時要核對成分），
  再補其他人用許可最多 DETAIL_BACKFILL 張（環境變數 PERTENTO_DETAIL_BACKFILL，預設 1500；幾週內全部補齊）。
  詳細資料抓不到不擋排程（該列沒有 formula，補收程式下次再試）；成分空白的過 7 天重抓。有快取的列寫上 formula。
- scripts/add_current_licenses.py --download 會先跑 fetch() 並寫 RAW_FILE＋RAW_META；同一次排程 license_refresh
  再呼叫 fetch() 時，RAW_META 在 REUSE_HOURS 內、筆數相符就直接沿用（不重查 pertento）。
"""
import importlib.util
import json
import os
import sys
import time
from pathlib import Path

RAW_FILE = "raw/pertento_status.json"
RAW_META = "raw/pertento_status.meta.json"     # add_current_licenses.py --download 寫：fetched_at、筆數（同次排程沿用）
FORMULA_FILE = "raw/pertento_formula.json"     # 詳細資料的成分快取（newcode → fml…）
REUSE_HOURS = 6
DETAIL_BACKFILL = int(os.environ.get("PERTENTO_DETAIL_BACKFILL", "1500"))
FIELDS = ("brand_name_th", "brand_name_en", "license_holder", "legal_category", "dosage_form", "newcode")
REPO = Path(__file__).resolve().parents[1]
CURRENT: set = set()   # fetch() 填：pertento 查到的全部許可證號（含註銷）；空的就不判定
MIN_CURRENT = 20000    # 2026-11-16 下載 30,171 列、27,228 個號
NOT_LISTED = "ไม่พบเลขทะเบียนนี้ในระบบค้นหาข้อมูลผลิตภัณฑ์ยาของ อย. (สถานะไม่ทราบ)"


def _pt():
    p = Path(__file__).resolve().parent / "_pertento.py"
    s = importlib.util.spec_from_file_location("_pertento", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def _terms():
    out = set()
    for f in (REPO / "data/bundles").glob("*/drug_bundle.json"):
        out |= {t.strip() for t in ((json.loads(f.read_text(encoding="utf-8")).get("thaifda") or {}).get("query_terms") or []) if t.strip()}
    return sorted(out)


def _bundles():
    out = {}
    for f in sorted((REPO / "data/bundles").glob("*/drug_bundle.json")):
        out[f.parent.name] = json.loads(f.read_text(encoding="utf-8")).get("thaifda") or {}
    return out


def _search_all():
    from concurrent.futures import ThreadPoolExecutor
    pt = _pt()
    terms = _terms()
    if not terms:
        raise RuntimeError("證據包沒有 thaifda.query_terms（先跑 th_rebuild_licenses_20261031.py）")

    def one(t):
        rows, total = pt.search(t)
        if len(rows) < (total or 0):
            raise RuntimeError(f"{t}：只取到 {len(rows)}/{total} 筆，翻頁失敗")
        print(f"pertento {t}: {len(rows)}", file=sys.stderr, flush=True)
        return [{"id": r["license_id"].strip(), "status": r["status"], "term": t, **{k: r.get(k, "") for k in FIELDS}} for r in rows]

    with ThreadPoolExecutor(4) as ex:
        return [x for part in ex.map(one, terms) for x in part]


def _reuse():
    """同一次排程裡 add_current_licenses.py --download 剛查過：沿用 RAW_FILE（筆數相符、有新欄位才算）"""
    meta, raw = REPO / "data" / RAW_META, REPO / "data" / RAW_FILE
    try:
        m = json.loads(meta.read_text(encoding="utf-8"))
        rows = json.loads(raw.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if time.time() - m.get("fetched_at", 0) > REUSE_HOURS * 3600 or len(rows) != m.get("rows") or not rows or "newcode" not in rows[0]:
        return None
    print(f"沿用 {RAW_FILE}（{len(rows)} 列，{time.strftime('%Y-%m-%d %H:%M', time.gmtime(m['fetched_at']))} UTC 查的）", file=sys.stderr)
    return rows


def candidate_newcodes(rows, bundles=None):
    """每個證據包：查詢詞查得到、該證據包還沒有（records 與 excluded_records）的人用許可 → newcode"""
    pt = _pt()
    bundles = _bundles() if bundles is None else bundles
    by_term = {}
    for x in rows:
        by_term.setdefault(x["term"].strip(), []).append(x)
    need = set()
    for th in bundles.values():
        have = {str(r.get("license_id") or "").strip() for k in ("records", "excluded_records") for r in th.get(k) or []}
        for t in th.get("query_terms") or []:
            for x in by_term.get(t.strip(), []):
                if pt.HUMAN.match(x["id"]) and x["id"] not in have and x.get("newcode"):
                    need.add(x["newcode"])
    return need


def _formula_entry(d):
    return {"fml": [str(f.get("FML_NAME") or "").strip() for f in d.get("XML_DRUG_FORMULA") or [] if str(f.get("FML_NAME") or "").strip()],
            "status_name": d.get("STATUS_NAME") or "", "app_date": d.get("APP_DATE") or "",
            "fetched": time.strftime("%Y-%m-%d")}


def attach_formula(rows, bundles=None, backfill=None):
    """詳細資料的成分補進 FORMULA_FILE（先補補收候選，再補其他人用許可最多 backfill 張），有快取的列寫上 formula。回傳 (新抓, 失敗)"""
    import threading
    from concurrent.futures import ThreadPoolExecutor
    pt = _pt()
    path = REPO / "data" / FORMULA_FILE
    cache = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    backfill = DETAIL_BACKFILL if backfill is None else backfill
    stale = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 7 * 86400))
    def missing(nc):
        e = cache.get(nc)
        return e is None or (not e.get("fml") and e.get("fetched", "") < stale)
    need = sorted(nc for nc in candidate_newcodes(rows, bundles) if missing(nc))
    rest = sorted({x["newcode"] for x in rows if x.get("newcode") and pt.HUMAN.match(x["id"]) and missing(x["newcode"])} - set(need))
    todo = need + rest[:max(0, backfill)]
    lock, tl, fail = threading.Lock(), threading.local(), []

    def one(nc):
        if not hasattr(tl, "s"):
            tl.s = pt.detail_session()
        try:
            e = _formula_entry(pt.detail(tl.s, nc))
        except Exception as ex:  # 抓不到不擋排程，下次再試
            with lock:
                fail.append(nc)
            tl.s = pt.detail_session()
            return
        with lock:
            cache[nc] = e
            if len(cache) % 200 == 0:
                path.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")
    if todo:
        print(f"pertento 詳細資料：補收候選 {len(need)}、其他 {len(todo) - len(need)} 張", file=sys.stderr, flush=True)
        with ThreadPoolExecutor(3) as ex:
            list(ex.map(one, todo))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")
    for x in rows:
        e = cache.get(x.get("newcode") or "")
        if e is not None:
            x["formula"] = e["fml"]
    return len(todo) - len(fail), fail


def fetch(reuse=True):
    """reuse＝False：一定重查（add_current_licenses.py --download 用）"""
    out = _reuse() if reuse else None
    if out is None:
        out = _search_all()
        try:
            n, fail = attach_formula(out)
            if fail:
                print(f"pertento 詳細資料抓不到 {len(fail)} 張（下次再試）", file=sys.stderr)
        except Exception as e:  # 成分是補收用的附加資料，失敗不擋狀態更新
            print(f"pertento 詳細資料略過：{e}", file=sys.stderr)
    CURRENT.clear()
    if len({x["id"] for x in out}) >= MIN_CURRENT:
        CURRENT.update(x["id"] for x in out)
    return out


def confirmed_absent(lid):
    """給 license_refresh：pertento 依成分查完整、查無此號（含註銷也沒有）＝確認系統已不列；狀態未知，不是註銷"""
    lid = str(lid).strip()
    return bool(CURRENT) and bool(lid) and lid not in CURRENT


def preprocess(bundle):
    """pertento 查無的號標 unknown＋pertento_not_listed；又出現就還原。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("thaifda") or {}).get("records") or []:
        lid = record_id(r)
        if not lid:
            continue
        if lid in CURRENT:
            if r.get("pertento_not_listed"):
                r.pop("pertento_not_listed", None)
                r["status"] = r.pop("status_before_pertento_not_listed", "")
                r["license_status"] = _pt().status_of(r["status"]) or r.get("license_status")
                ch = True
        elif not r.get("pertento_not_listed"):
            r["status_before_pertento_not_listed"] = r.get("status") or ""
            r["status"] = NOT_LISTED
            r["license_status"] = "unknown"
            r["pertento_not_listed"] = today
            ch = True
    return ch


def validate(new, old):
    p = []
    bad = sorted({x["status"] for x in new if _pt().status_of(x["status"]) is None})
    if bad:
        p.append(f"認不得的狀態原文：{bad[:10]}")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    pt = _pt()
    out = {}
    for x in new:  # 同號多列：有任一列有效就取有效那列，否則取第一列（與重建時相同）
        if x["id"] not in out or (pt.status_of(x["status"]) == "valid" and pt.status_of(out[x["id"]]) != "valid"):
            out[x["id"]] = x["status"]
    return out


def record_id(rec):
    return str(rec.get("license_id") or "").strip() if rec.get("source") == "Thai FDA pertento" else ""


def update(rec, new):
    st = _pt().status_of(new)
    if rec.get("status") == new and rec.get("license_status") == st:
        return False
    rec["status"], rec["license_status"] = new, st
    return True


# 2026-11-24：市場段落的許可證表改成程式產生（scripts/sync_license_tables.py，用戶決定）。
# 每週排程 3b 自我檢查：程式區塊裡表格列以外的行（標記、超過 30 張的說明句、沒有紀錄句）也算程式產生的行。
# 2026-11-24 第三輪起含 add_section 補的市場段落標題。
PAGE_NOTE = (r"^(## ข้อมูลการวางจำหน่ายในประเทศไทย|ตารางนี้แสดงไม่เกิน 30 รายการ \(ทะเบียนที่ยังมีผลก่อน\) รายการทั้งหมดดูได้ที่ระบบค้นหาข้อมูลผลิตภัณฑ์ยาของ อย\. "
             r"\(https://pertento\.fda\.moph\.go\.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG\.aspx\)( ข้อมูลที่ใช้ในรายงานนี้มีทะเบียนตำรับยาทั้งหมด \d+ รายการ)?|"
             r"ไม่พบทะเบียนตำรับยาในระบบค้นหาข้อมูลผลิตภัณฑ์ยาของ อย\.|<!-- licenses:(begin|end) -->)$")


def sync_tables(site_dir, bundles):
    """狀態有變的藥，程式許可證表依證據包重排（有效的在前、最多 30 列）；全站都跑（便宜），回傳改到的頁"""
    s = importlib.util.spec_from_file_location("th_slt", Path(site_dir) / "scripts/sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return [(pg, "許可證表", "", "依證據包重排") for pg in m.run()]
