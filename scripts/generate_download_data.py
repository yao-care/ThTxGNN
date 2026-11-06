#!/usr/bin/env python3
"""ThTxGNN 的下載檔產生器（2026-11-06 起；本站自己的，不與他站共用）。

產生 5 份檔（網址沿用 2026-03 舊程式 generate_thai_website.py 產的檔，欄位與格式照舊）：

  docs/downloads/thtxgnn_drugs_summary.json   全部公開藥物，JSON list
  docs/downloads/thtxgnn_drugs_summary.csv    同上，CSV
  docs/downloads/thtxgnn_high_evidence.csv    其中頁首等級 L1–L4 的藥
  docs/data/drugs.csv                         與 thtxgnn_drugs_summary.csv 相同
  docs/data/drugs-by-level.json               同一份資料依頁首等級分組（L1…L5、N/A）

只讀網站現行內容，不讀 data/，不手寫藥品資料：

  - 只收公開藥物頁（docs/_drugs/*.md，排除 noindex 頁與轉址頁）；筆數＝docs/_data/drug_stats.json 的 total_drugs。
  - slug＝藥物頁檔名、name＝front matter title、evidence_level＝front matter evidence_level（頁首等級，沒寫當 L5）、
    indication_count＝front matter indication_count、url＝該頁網址。
  - predicted_indication、txgnn_score：docs/data/search-index.json 裡該藥分數最高的一筆預測（分數同分取索引中較前者），
    分數由百分比換成 0–1、4 位小數。這就是藥物頁「ภาพรวมฉบับย่อ」表的「ข้อบ่งใช้ใหม่ที่ทำนาย」與「คะแนนการทำนาย TxGNN」
    （2026-11-06 實查 145 藥全部一致）。沒有預測的藥（頁首 N/A）兩欄留空。
  - original_indication：藥物頁「ภาพรวมฉบับย่อ」表「ข้อบ่งใช้เดิม」列；頁面寫「ไม่มีบันทึกในข้อมูลท้องถิ่น」、「-」或沒有這列時留空
    （search-index 的 original 欄是舊程式留下的值，與頁面不一致，不用）。
  - decision：同表「คำแนะนำในการตัดสินใจ」列原文（Hold、Proceed with Guardrails…）；沒有這列時留空。
  - thailand_approved：同表「สถานะการวางจำหน่ายในไทย」列。寫「วางจำหน่าย (ทะเบียนที่ยังมีผล N จาก M รายการ)」且 N>0 → True；
    寫「ไม่พบทะเบียนที่ยังมีผล …（ทะเบียนที่ถูกยกเลิก N จาก N รายการ）」（全部已註銷）→ False；其他（查無登記、沒有這列）留空
    （JSON 為 null）。
  - drugbank_id、license_id：網站現行內容沒有可靠來源，留空（舊檔的 license_id 2026-10-31 已因編造清空）。

內容沒變就不改寫檔案。docs/data/drugs.json、search-index.json 有變（藥物頁改等級、改 noindex、重產預測）之後要重跑；
scripts/check_seo_docs.py 第 13 項會擋過期的檔。

用法：python3 scripts/generate_download_data.py            # 產生（有變才寫）
      python3 scripts/generate_download_data.py --check    # 只比對，有不同就 exit 1
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

FIELDS = ["slug", "name", "drugbank_id", "license_id", "evidence_level", "indication_count",
          "original_indication", "predicted_indication", "txgnn_score", "thailand_approved", "decision", "url"]
LEVEL_ORDER = ["L1", "L2", "L3", "L4", "L5", "N/A"]
HIGH_LEVELS = ("L1", "L2", "L3", "L4")

OUTPUTS = {
    "summary_json": "downloads/thtxgnn_drugs_summary.json",
    "summary_csv": "downloads/thtxgnn_drugs_summary.csv",
    "high_csv": "downloads/thtxgnn_high_evidence.csv",
    "data_csv": "data/drugs.csv",
    "by_level_json": "data/drugs-by-level.json",
}

ROW_ORIG = "ข้อบ่งใช้เดิม"
ROW_DECISION = "คำแนะนำในการตัดสินใจ"
ROW_AVAIL = "สถานะการวางจำหน่ายในไทย"
NO_RECORD = {"", "-", "—", "ไม่มีบันทึกในข้อมูลท้องถิ่น"}
AVAIL_YES = re.compile(r"^วางจำหน่าย \(ทะเบียนที่ยังมีผล (\d+) จาก (\d+) รายการ\)$")
AVAIL_NO = re.compile(r"^ไม่พบทะเบียนที่ยังมีผล.*\(ทะเบียนที่ถูกยกเลิก (\d+) จาก (\d+) รายการ\)$")


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    out = {}
    for line in text[3:end if end >= 0 else None].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def jekyll_slugify(s):
    return re.sub(r"[\W_]+", "-", s).strip("-").lower()


def overview_row(text, key):
    """「ภาพรวมฉบับย่อ」表的某一列（整頁第一個符合的兩欄列）。"""
    m = re.search(r"^\|\s*" + re.escape(key) + r"\s*\|\s*(.*?)\s*\|\s*$", text, re.M)
    return m.group(1).strip() if m else None


def is_public(text, fm):
    redirect = 'http-equiv="refresh"' in text or fm.get("layout") == "id_redirect" or bool(fm.get("redirect_to"))
    return not redirect and fm.get("noindex", "").lower() != "true"


def thailand_approved(value):
    if value is None:
        return None
    m = AVAIL_YES.match(value)
    if m:
        return True if int(m.group(1)) > 0 else None
    m = AVAIL_NO.match(value)
    if m and m.group(1) == m.group(2):
        return False
    return None


def build_records(docs=DOCS):
    index = json.loads((docs / "data" / "search-index.json").read_text(encoding="utf-8"))
    by_slug = {d.get("slug"): d for d in index.get("drugs", [])}
    records, warnings = [], []
    for f in sorted((docs / "_drugs").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        if not is_public(text, fm):
            continue
        url_slug = jekyll_slugify(fm.get("slug") or f.stem)
        url = fm.get("permalink") or f"/drugs/{url_slug}/"
        pred, score = "", ""
        entry = by_slug.get(url_slug)
        if entry is None:
            warnings.append(f"{f.name}：search-index.json 沒有 {url_slug}，predicted_indication／txgnn_score 留空")
        elif entry.get("indications"):
            best = entry["indications"][0]
            for ind in entry["indications"]:
                if float(ind.get("score") or 0) > float(best.get("score") or 0):
                    best = ind
            pred = best.get("name", "")
            if best.get("score") not in (None, ""):
                score = f"{float(best['score']) / 100:.4f}"
        orig = overview_row(text, ROW_ORIG)
        decision = overview_row(text, ROW_DECISION)
        try:
            count = int(fm.get("indication_count") or 0)
        except ValueError:
            count = 0
        records.append({
            "slug": f.stem,
            "name": fm.get("title", f.stem),
            "drugbank_id": "",
            "license_id": "",
            "evidence_level": fm.get("evidence_level") or "L5",
            "indication_count": count,
            "original_indication": "" if orig is None or orig in NO_RECORD else orig,
            "predicted_indication": pred,
            "txgnn_score": score,
            "thailand_approved": thailand_approved(overview_row(text, ROW_AVAIL)),
            "decision": decision or "",
            "url": url,
        })
    return records, warnings


def to_csv(records):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    w.writeheader()
    for r in records:
        row = dict(r)
        row["thailand_approved"] = "" if r["thailand_approved"] is None else str(r["thailand_approved"])
        w.writerow(row)
    return buf.getvalue().encode("utf-8")


def to_json(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")


def build(docs=DOCS):
    """回傳 ({docs 相對路徑: bytes}, records, warnings)。"""
    records, warnings = build_records(docs)
    by_level = {}
    for lv in LEVEL_ORDER + sorted({r["evidence_level"] for r in records} - set(LEVEL_ORDER)):
        group = [r for r in records if r["evidence_level"] == lv]
        if group:
            by_level[lv] = group
    summary_csv = to_csv(records)
    files = {
        OUTPUTS["summary_json"]: to_json(records),
        OUTPUTS["summary_csv"]: summary_csv,
        OUTPUTS["high_csv"]: to_csv([r for r in records if r["evidence_level"] in HIGH_LEVELS]),
        OUTPUTS["data_csv"]: summary_csv,
        OUTPUTS["by_level_json"]: to_json(by_level),
    }
    return files, records, warnings


def main():
    check = "--check" in sys.argv[1:]
    files, records, warnings = build()
    for w in warnings:
        print(f"⚠ {w}")
    changed = []
    for rel, data in files.items():
        path = DOCS / rel
        if path.exists() and path.read_bytes() == data:
            continue
        changed.append(rel)
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    dist = {lv: sum(r["evidence_level"] == lv for r in records) for lv in LEVEL_ORDER}
    print(f"公開藥物頁 {len(records)} 個；等級 {dist}；高證據（L1–L4）{sum(dist[l] for l in HIGH_LEVELS)} 個")
    if check:
        if changed:
            print("與產生器輸出不同：" + "、".join(changed))
            sys.exit(1)
        print("5 份下載檔與產生器輸出相同")
    else:
        print(("已更新：" + "、".join(changed)) if changed else "內容沒變，沒有改寫檔案")


if __name__ == "__main__":
    main()
