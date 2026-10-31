"""TH（Thai FDA 公開查詢系統 pertento）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-31）。

2026-10-31：原本的許可證號是程式編造的（見 .claude/th_rebuild_licenses_20261031.py），已改用 pertento 的真實許可證。
pertento 依成分查詢、不用登入（GitHub runner 實測翻頁、詳細資料都可用，run 41148774713；paracetamol 2741 筆約 15 分鐘）；
查詢詞＝證據包 thaifda.query_terms（主名稱＋別名），4 路並行。只更新證據包裡已有許可證的狀態，不新增許可證。
寫回：status＝pertento 原文（คงอยู่／ยกเลิก(日期)／ปลด SMP…），license_status＝valid／cancelled。新資料查不到的許可證保留原狀態。
"""
import importlib.util
import json
import sys
from pathlib import Path

RAW_FILE = "raw/pertento_status.json"
REPO = Path(__file__).resolve().parents[1]


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
        return [x for part in ex.map(one, terms) for x in part]


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
