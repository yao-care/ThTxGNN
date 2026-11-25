#!/usr/bin/env python3
"""補收 pertento 查得到、證據包還沒有的本藥許可證（2026-11-25 第六輪，用戶決定「新許可補收：全部照原規則補」）。

證據包的 thaifda 區塊是 2026-10-31 母目錄 .claude/th_rebuild_licenses_20261031.py 一次重建的：每個藥用 thaifda.query_terms
（主名稱＋別名）在 Thai FDA pertento 依成分查詢，只留人用許可證（號碼第二碼 A/B/C），查詢詞「部分比對」帶進來的別的藥
（查 Estradiol 也會出現 ethinyl estradiol、查 Prednisolone 也會出現 methylprednisolone）逐張開詳細資料核對成分，
成分名不是以本藥名稱開頭的排除。之後每週排程（scripts/license_adapter.py）只更新已有許可證的狀態，不新增許可證，
所以 10-31 之後核准的許可證收不進來（2026-11-25 第五輪調查：6 張）。

規則（同 10-31 重建，不放寬）：
- 查詢結果＝RAW_FILE（adapter.fetch() 每列存品名、持有人、法定類別、劑型、newcode；--download 時當場查）。
- 證據包查詢詞查得到、證據包 records／excluded_records 都沒有的人用許可證（同號多列取有效那列，同重建）是候選。
- 候選一律核對詳細資料成分（FORMULA_FILE，adapter 補的快取）：有一個成分名（去掉序號、SODIUM 等陽離子字首）以查詢詞開頭、
  後面是結尾或非字母（鹽類、酯類）＝本藥，補一筆（欄位同重建，另記 added、added_basis）。10-31 只核對「兩邊都出現」的列，
  這裡全部核對，只會比原規則少收、不會多收別的藥。
- 成分欄空白的不收、列出；還沒有詳細資料的這次不判定（下次排程再試）；成分不是本藥的照原規則不收（只計數）。
- 原收集器沒有筆數上限（每張許可證一筆、total_matches＝不重複許可證數），所以沒有「算進總數卻沒存」的號，不用回填。
- 停損：證據包 total_matches ≠ records 裡 pertento 許可證的不重複號碼數，整包不補、列出。
只加不刪、可重複執行（第二次跑 0 筆）。每週 license-refresh.yml 在 license_refresh 前以 --download 跑（失敗不擋排程）。
用法（repo 根目錄，先還原 data/）：python3 scripts/add_current_licenses.py [--download] [--dry-run] [--report out.tsv]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATION = re.compile(r"^(SODIUM|POTASSIUM|CALCIUM|MAGNESIUM|DISODIUM|DIPOTASSIUM)\s+")   # 同 th_rebuild_licenses_20261031.py


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


ad = _load("th_adapter", ROOT / "scripts/license_adapter.py")
pt = _load("th_pertento", ROOT / "scripts/_pertento.py")


def _norm(x):
    x = re.sub(r"^\s*\d+\s*\.\s*", "", str(x or "")).upper().replace("SULPH", "SULF")
    return " ".join(x.split())


def formula_has(fml, terms):
    """同 th_rebuild_licenses_20261031.formula_has：成分名以本藥名稱（或別名）開頭，後面是結尾或非字母"""
    ts = [_norm(t) for t in terms]
    for f in fml:
        n = _norm(f)
        for t in ts:
            m = n if CATION.match(t) else CATION.sub("", n)
            if m.startswith(t) and (len(m) == len(t) or not m[len(t)].isalpha()):
                return True
    return False


def own_ids(th):
    return {str(r.get("license_id") or "").strip() for r in th.get("records") or [] if r.get("source") == "Thai FDA pertento"}


def download():
    raw, meta = ROOT / "data" / ad.RAW_FILE, ROOT / "data" / ad.RAW_META
    old = json.loads(raw.read_text(encoding="utf-8")) if raw.exists() else None
    fp = ROOT / "data" / ad.FORMULA_FILE
    n0 = len(json.loads(fp.read_text(encoding="utf-8"))) if fp.exists() else 0
    rows = ad.fetch(reuse=False)
    n1 = len(json.loads(fp.read_text(encoding="utf-8"))) if fp.exists() else 0
    print(f"詳細資料成分快取：新增 {n1 - n0} 張（共 {n1}）")
    probs = ad.validate(rows, old)
    if len({x["id"] for x in rows}) < ad.MIN_CURRENT:
        probs.append(f"許可證號只有 {len({x['id'] for x in rows})} 個（少於 {ad.MIN_CURRENT}）")
    if probs:
        sys.exit("pertento 查詢結果有問題，不補收：" + "；".join(probs))
    raw.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    meta.write_text(json.dumps({"fetched_at": time.time(), "rows": len(rows)}), encoding="utf-8")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true", help="當場查 pertento（並補詳細資料成分），寫 RAW_FILE")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report")
    a = ap.parse_args()
    if a.download:
        rows = download()
    else:
        rows = json.loads((ROOT / "data" / ad.RAW_FILE).read_text(encoding="utf-8"))
        if not rows or "newcode" not in rows[0]:
            sys.exit(f"{ad.RAW_FILE} 沒有 newcode 等欄位（舊格式），先跑 --download")
    fp = ROOT / "data" / ad.FORMULA_FILE
    cache = json.loads(fp.read_text(encoding="utf-8")) if fp.exists() else {}
    when = time.strftime("%Y-%m-%d", time.gmtime((json.loads((ROOT / "data" / ad.RAW_META).read_text()) or {}).get("fetched_at", time.time()))) \
        if (ROOT / "data" / ad.RAW_META).exists() else "?"
    by_term = {}
    for x in rows:
        by_term.setdefault(x["term"].strip(), []).append(x)
    today = time.strftime("%Y-%m-%d")
    stats = {"bundles": 0, "added": 0, "other_drug": 0, "empty_formula": 0, "no_detail": 0, "stopped": []}
    report = []
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        th = b.get("thaifda") or {}
        terms = [t.strip() for t in th.get("query_terms") or [] if t.strip()]
        if not terms:
            continue
        own = own_ids(th)
        if th.get("total_matches") != len(own):
            stats["stopped"].append(f"{name}（total_matches {th.get('total_matches')}≠{len(own)}）")
            continue
        have = own | {str(r.get("license_id") or "").strip() for r in th.get("excluded_records") or []}
        cand = {}
        for t in terms:
            for x in by_term.get(t, []):
                lid = x["id"].strip()
                if not lid or lid in have or not pt.HUMAN.match(lid):
                    continue
                cand.setdefault(lid, []).append(x)
        new = []
        for lid, xs in sorted(cand.items()):
            xs.sort(key=lambda x: pt.status_of(x["status"]) != "valid")   # 同號多列：有效那列優先（同重建）
            r = xs[0]
            fml = next((cache[x["newcode"]]["fml"] for x in xs if x.get("newcode") in cache), None)
            st = pt.status_of(r["status"])
            if fml is None:
                kind = "no_detail"
            elif not fml:
                kind = "empty_formula"
            elif not formula_has(fml, terms):
                kind = "other_drug"
            elif st is None:
                kind = "unknown_status"
            else:
                kind = "added"
            report.append((name, lid, r.get("brand_name_en") or r.get("brand_name_th"), r.get("dosage_form"), r["status"], kind, " + ".join(fml or [])))
            if kind == "unknown_status":
                print(f"認不得的狀態 {name} {lid}：{r['status']}", file=sys.stderr)
                continue
            stats[kind] += 1 if kind != "added" else 0
            if kind != "added":
                continue
            new.append({"license_id": lid, "brand_name_th": r.get("brand_name_th", ""), "brand_name_en": r.get("brand_name_en", ""),
                        "license_holder": r.get("license_holder", ""), "legal_category": r.get("legal_category", ""),
                        "dosage_form": r.get("dosage_form", ""), "status": r["status"], "license_status": st, "kind": pt.kind_of(lid),
                        "newcode": r.get("newcode", ""), "source": "Thai FDA pertento", "added": today,
                        "added_basis": f"pertento 依成分查詢（{when}，查詢詞 {r['term']}）＋詳細資料成分 {' + '.join(fml)}；規則同 2026-10-31 重建"})
        if not new:
            continue
        stats["bundles"] += 1
        stats["added"] += len(new)
        print(f"{name}：補 {len(new)} 張（{', '.join(x['license_id'] + ' ' + x['brand_name_en'] for x in new)}）")
        if a.dry_run:
            continue
        th["records"] = (th.get("records") or []) + new
        th["total_matches"] = len(own) + len(new)
        th["found"] = True
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if a.report:
        Path(a.report).write_text("bundle\tlicense_id\tbrand\tform\tstatus\tresult\tformula\n" +
                                  "".join("\t".join(map(str, r)) + "\n" for r in report), encoding="utf-8")
    print(f"補收：{stats['bundles']} 個證據包、{stats['added']} 張許可證；不收：成分不是本藥 {stats['other_drug']}、"
          f"成分欄空白 {stats['empty_formula']}、還沒有詳細資料 {stats['no_detail']}；停損 {len(stats['stopped'])} 包"
          + (f"（{'；'.join(stats['stopped'])}）" if stats["stopped"] else "") + ("（試跑，沒寫入）" if a.dry_run else ""))


if __name__ == "__main__":
    main()
