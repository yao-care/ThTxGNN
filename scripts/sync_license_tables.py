#!/usr/bin/env python3
"""藥物頁「## ข้อมูลการวางจำหน่ายในประเทศไทย」段落的許可證表一律由程式依證據包產生（2026-11-24，用戶決定）。

為什麼：每週許可證排程（母目錄 license_refresh_20261029.py）只改程式管得到的格子。本站 2026-10-31 由母目錄
th_rebuild_licenses_20261031.py 一次性產生過許可證表（沒有標記、之後只靠排程同步狀態格，列的排序與增減不會跟上），
本支把那套寫法變成每次都跑的程式：
- 段落裡的第一張表（或 10-31 寫的「ไม่พบทะเบียนตำรับยา…」一句）換成程式區塊，前後加
  「<!-- licenses:begin -->」「<!-- licenses:end -->」標記；已有標記就換掉標記之間的內容。
  段落裡沒有表的頁（chlorpheniramine、pravastatin）把程式區塊放在段落開頭。
- 表頭「| เลขทะเบียน | ผลิตภัณฑ์ | รูปแบบยา | สถานะ |」（10-31 的寫法）；只收證據包 thaifda.records 裡 source＝Thai FDA pertento 的紀錄
  （NLEM 紀錄沒有許可證號）；同號只取一列（有任一列有效取有效那列）；有效的在前、其餘照證據包順序；最多 30 列。
  品名取英文品名（沒有就泰文）、劑型照 pertento 原文（不翻譯）；狀態格＝pertento 原文（คงอยู่／ยกเลิก(日期)／ปลด SMP…；
  pertento 查無的號是 license_adapter.NOT_LISTED 那句，狀態未知）。
- 超過 30 張：表下一句 MORE（10-31 的寫法，指向 pertento）；超過 30 張時另寫總數 TOTAL_NOTE。
- 證據包沒有任何 pertento 紀錄：區塊內只放 NONE_LINE。
- 段落裡、程式區塊外跟程式句相同的行（以前重排時重複插入的）一併拿掉。
- 整頁沒有市場段落、證據包有 pertento 紀錄的公開頁：在安全性／結論／查核紀錄／免責聲明段之前補段落與程式表（add_section，2026-11-24 第三輪）。
資料來源兩種：bundle（data/bundles；每週排程 adapter 的 sync_tables、手動）與 snapshot
（snapshots/th_licenses.json.gz 的 rows／total；scripts/apply_drug_reviews.py 結尾、scripts/build_license_snapshot.py 結尾，不需要 data/）。
gate（src/thtxgnn/regulatory/licenses.py 的 program_block_problems）擋「段落有表卻不是程式區塊」「程式區塊≠快照重算結果」。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--from-snapshot] [--dry-run] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = "## ข้อมูลการวางจำหน่ายในประเทศไทย"
HEAD = ["| เลขทะเบียน | ผลิตภัณฑ์ | รูปแบบยา | สถานะ |", "|------|------|------|------|"]
CAP = 30
SRC = "Thai FDA pertento"
MORE = ("ตารางนี้แสดงไม่เกิน 30 รายการ (ทะเบียนที่ยังมีผลก่อน) "
        "รายการทั้งหมดดูได้ที่ระบบค้นหาข้อมูลผลิตภัณฑ์ยาของ อย. (https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx)")
TOTAL_NOTE = "ข้อมูลที่ใช้ในรายงานนี้มีทะเบียนตำรับยาทั้งหมด {m} รายการ"
NONE_LINE = "ไม่พบทะเบียนตำรับยาในระบบค้นหาข้อมูลผลิตภัณฑ์ยาของ อย."
BEGIN, END = "<!-- licenses:begin -->", "<!-- licenses:end -->"
NOTE_RX = (r"^(" + re.escape(MORE) + r"( ข้อมูลที่ใช้ในรายงานนี้มีทะเบียนตำรับยาทั้งหมด \d+ รายการ)?|" + re.escape(NONE_LINE)
           + r"|<!-- licenses:(begin|end) -->)$")
SNAP = ROOT / "snapshots" / "th_licenses.json.gz"


def _cell(x, n):
    return re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()[:n]


def table_rows(recs):
    """證據包紀錄 → 表格列（全部）。規則同 10-31 th_rebuild_licenses_20261031.table()／records_from()"""
    by = {}
    for r in recs or []:
        if r.get("source") != SRC:
            continue
        lid = str(r.get("license_id") or "").strip()
        if not lid:
            continue
        if lid not in by or (r.get("license_status") == "valid" and by[lid].get("license_status") != "valid"):
            by[lid] = r
    lic = sorted(by.values(), key=lambda r: r.get("license_status") != "valid")  # 穩定排序：其餘照證據包順序
    return [f"| {str(r['license_id']).strip()} | {_cell(r.get('brand_name_en') or r.get('brand_name_th'), 60)} | "
            f"{_cell(r.get('dosage_form'), 40)} | {_cell(r.get('status'), 120)} |" for r in lic]


def rows_of(tf):
    """快照用：(前 CAP 列, 總張數)"""
    rows = table_rows((tf or {}).get("records") or [])
    return rows[:CAP], len(rows)


def program_block(rows, total):
    if not rows:
        return [NONE_LINE]
    out = HEAD + rows[:CAP]
    if total > CAP:
        out += ["", MORE + " " + TOTAL_NOTE.format(m=total)]
    return out


def _section(lines):
    if SEC not in lines:
        return None, None
    a = lines.index(SEC) + 1
    return a, next((k for k in range(a, len(lines)) if re.match(r"^#{1,2} ", lines[k])), len(lines))


def _is_note(l):
    s = l.strip()
    return s == NONE_LINE or s.startswith(MORE)


def process(text, rows, total, blk=None):
    lines = text.split("\n")
    a, b = _section(lines)
    if a is None:
        return (add_section(text, rows, total) if blk is None else None) or text
    blk = blk or [BEGIN, ""] + program_block(rows, total) + ["", END]
    sec = lines[a:b]
    if BEGIN in sec and END in sec:
        x, y = lines.index(BEGIN, a), lines.index(END, a)
    else:
        tb = [k for k in range(a, b) if lines[k].startswith("|")]
        nl = [k for k in range(a, b) if lines[k].strip() == NONE_LINE]
        if tb:
            x = y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
        elif nl:
            x = y = nl[0]
        else:
            x, y = a, a - 1  # 段落沒有表：放在段落開頭
    head = lines[:x]
    while head and not head[-1].strip():
        head.pop()
    rest = [l for l in lines[y + 1:b] if not _is_note(l)]
    while rest and not rest[0].strip():
        rest.pop(0)
    out = head + [""] + blk + [""] + rest
    if b < len(lines) and out[-1].strip():
        out.append("")
    out += lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁沒有「## ข้อมูลการวางจำหน่ายในประเทศไทย」段落、但證據包有 pertento 紀錄的，
# 補一個段落放程式表。位置：「## ข้อพิจารณาด้านความปลอดภัย」（安全性）之前；沒有就「## สรุปและขั้นตอนถัดไป」（結論）之前；
# 再沒有就「## บันทึกการตรวจสอบ」（查核紀錄）、「## ข้อจำกัดความรับผิดชอบ」（免責聲明）之前。noindex 頁與證據包沒有紀錄的頁不補。
ADD_BEFORE = ("ข้อพิจารณาด้านความปลอดภัย", "สรุปและขั้นตอนถัดไป", "บันทึกการตรวจสอบ", "ข้อจำกัดความรับผิดชอบ")


def add_section(text, rows, total):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    if re.search(r"^noindex:\s*true", fm, re.M) or not rows:
        return None
    lines = text.split("\n")
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    k = at - 1
    while k > 0 and not lines[k].strip():
        k -= 1
    if lines[k].strip() == "<!-- review:begin log -->":  # 查核紀錄段的標題在 log 區塊裡：段落放在區塊之前（否則套用查核紀錄時會被當成 log 區塊的內容）
        at = k
    sec = [SEC, "", BEGIN, ""] + program_block(rows, total) + ["", END, ""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落（取代新頁模型寫的第一張表；
    新頁段落沒有表時放在段落開頭）。舊頁沒有程式區塊就原樣回傳新頁。之後 apply_drug_reviews.py 會再依快照重排。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    return process(new_text, None, None, old[old.index(BEGIN):old.index(END) + 1])


def _snap():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in dict.fromkeys((stem, stem.replace("-", "_"), stem.replace("_", "-"))):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8")).get("thaifda") or {}
    return None


STATUS_ROW, KNOWN_ROW = "สถานะการวางจำหน่ายในไทย", "สถานะตลาดในประเทศไทย"
_ROW = re.compile(r"^\| (สถานะการวางจำหน่ายในไทย|สถานะตลาดในประเทศไทย) \|(.*)\|\s*$")


def sync_known_row(text):
    """已知用途頁的第二張概覽表另有一列「สถานะตลาดในประเทศไทย」（10-31 重建時寫的，跟「สถานะการวางจำหน่ายในไทย」列同一句）；
    每週排程的 sync_market_rows 只認後者，這列一直停在舊數字（2026-11-25 第六輪發現 3 頁）。照同頁狀態列的值同步。"""
    lines = text.split("\n")
    src = next((m.group(2) for m in map(_ROW.match, lines) if m and m.group(1) == STATUS_ROW), None)
    if src is None:
        return text
    for i, l in enumerate(lines):
        m = _ROW.match(l)
        if m and m.group(1) == KNOWN_ROW and m.group(2) != src:
            lines[i] = f"| {KNOWN_ROW} |{src}|"
    return "\n".join(lines)


def known_row_problems(text):
    """gate：同頁兩列的值要一樣"""
    vals = {}
    for l in text.split("\n"):
        m = _ROW.match(l)
        if m:
            vals.setdefault(m.group(1), m.group(2).strip())
    if KNOWN_ROW in vals and STATUS_ROW in vals and vals[KNOWN_ROW] != vals[STATUS_ROW]:
        return [f"「{KNOWN_ROW}」列（{vals[KNOWN_ROW]}）跟「{STATUS_ROW}」列（{vals[STATUS_ROW]}）不一致（跑 scripts/sync_license_tables.py）"]
    return []


def run(only=None, from_snapshot=False, dry=False):
    snap = _snap() if from_snapshot else None
    changed = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only and page.name not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        if from_snapshot:
            e = snap.get(page.stem)
            if not e or "rows" not in e:
                continue
            rows, total = e["rows"], e["total"]
        else:
            tf = _bundle(page.stem)
            if tf is None:
                continue
            rows, total = rows_of(tf)
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = sync_known_row(process(t0, rows, total))
        if new != t0:
            changed.append(page.stem)
            if not dry:
                page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = run({x for x in a if not x.startswith("--")} or None, "--from-snapshot" in a, "--dry-run" in a)
    print(f"許可證表（程式區塊）：改 {len(ch)} 頁" + ("（dry-run）" if "--dry-run" in a else ""))
