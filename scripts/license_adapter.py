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
"""
import importlib.util
import json
import sys
import time
from pathlib import Path

RAW_FILE = "raw/pertento_status.json"
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


def fetch():
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
        return [{"id": r["license_id"].strip(), "status": r["status"], "term": t} for r in rows]

    with ThreadPoolExecutor(4) as ex:
        out = [x for part in ex.map(one, terms) for x in part]
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
