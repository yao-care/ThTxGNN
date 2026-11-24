"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定；做法移植 KrTxGNN／MyTxGNN／HkTxGNN 的 count_prose，規則是本站泰文句型）。

用戶 2026-11-24 決定：正文裡「ใบอนุญาตทั้งหมด N รายการ ยังใช้ได้ V รายการ ยกเลิกแล้ว C รายการ」這類許可證張數敘述，
由程式依許可證快照（snapshots/th_licenses.json.gz 的 facts：total／valid／cancelled／unknown）改寫，每週資料更新後跟著改，
不逐筆寫查核紀錄（同 Tw／Kr／My：程式改寫的張數敘述是程式產生的正文）。

泰文不用句號、以空白分句，數字前後也有空白，所以不按「句子」切，而是逐行、逐個「數字＋單位」看左右的字：
  - 數字＝阿拉伯數字＋單位（รายการ／ฉบับ／ใบ／ทะเบียน／ตำรับ）；左邊 LEFT_WIN 個字內要有許可證字樣（ทะเบียน、ใบอนุญาต），
    或左邊緊接角色字（ยังใช้ได้、ยกเลิกแล้ว、ทั้งหมด…）而這一行有許可證字樣；左邊 LEFT_WIN 個字內有試驗／文獻／研究／
    交互作用等字樣（ลงทะเบียนการทดลอง 的「ทะเบียน」不算）的數字不是許可證張數，不看。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引用框、front matter。
  - 查核紀錄的 anchor（沒有 anchor 時 replacement）所在的文字裡的數字不改；要改的數字落在裡面時整行不動、列為 protected。
  - 數字不動（display）：顯示筆數（左邊緊接 แสดง、เพียง、ด้านล่าง、ข้างต้น、ตัวอย่าง、เช่น，或右邊緊接 ที่แสดง、ข้างต้น、ด้านล่าง）。
  - 整行不動（hedged/subset）：數字左邊的窗口有保留（อย่างน้อย、บางส่วน、ประมาณ、กว่า、เกิน）、相對數（อีก＋非「รอตรวจสอบสถานะ」、นอกจากนี้、
    ที่เหลือ）、劑型或廠商子集（ยาเม็ด、ยาฉีด、ครีม…、บริษัท、ผู้ผลิต、ผู้รับอนุญาต、mg）；事實層 partial 的頁整頁不動（本站目前沒有）。
角色（看數字左邊緊接的字與右邊幾個字）：ยกเลิก／ถูกยกเลิก→註銷；ยังใช้ได้／ใช้ได้／ยังมีผล／ยังมีผลบังคับใช้／ยังใช้งานได้ (valid)→有效；
右邊「…มีสถานะ “รอตรวจสอบสถานะ”」→狀態未知（事實層 unknown）；ทั้งหมด／รวม→總數；其餘→總數（同一行另有明確的有效／註銷數字時就是總數；
沒有時「N 張」可讀成總數或有效數，兩者相同才改，不同列為 ambiguous）。
同一行只要有一個許可證數字判斷不了，整行都不動（免得前後數字對不上）。
數字已等於該角色的事實就不動。原數字是 0（zero-premise）、要改成 0（to-zero）的不改、列出（前提變了，句子要人改）。
前提檢查（premise）：一行裡說「全部有效」（ยังใช้ได้ทั้งหมด／ทั้งหมดยังใช้ได้）而有效≠總數、說「全部註銷／沒有有效的」
（ทั้งหมด…ถูกยกเลิก、ไม่มีใบอนุญาตที่ยังมีผล…）而有效≠0、說「沒有註銷」而註銷≠0 時，整行不動、列出。
單方／複方張數（ยาเดี่ยว／สูตรผสม）只驗不改（列為 single-combo）。
"""
from __future__ import annotations

import re

from . import site as C

UNIT = r"(?:รายการ|ฉบับ|ใบ|ทะเบียน|ตำรับ)"
NUM = re.compile(r"(?<![\d/.,:A-Za-z])(\d[\d,]*)(\s*)(?:" + UNIT + r"(?!\s*/)|(?=จาก\s*\d[\d,]*\s*" + UNIT + r"))")  # 「V จาก N ใบ」的 V 也算
LICENSE = re.compile(r"(?<!ลง)ทะเบียน(?!การทดลอง)|ใบอนุญาต")
NOT_LICENSE = re.compile(r"การทดลอง|ทดลองทางคลินิก|NCT|PMID|วรรณกรรม|บทความ|การศึกษา|งานวิจัย|ปฏิกิริยาระหว่างยา|ผู้ป่วย|"
                         r"การคาดการณ์|คาดการณ์|ทำนาย|ข้อบ่งใช้|ตัวเลือก|อาการไม่พึงประสงค์|RCT|Phase|คะแนน|โมเดล")
LEFT_WIN = 45
HEDGED = re.compile(r"อย่างน้อย|บางส่วน|ประมาณ|กว่า|เกิน|ราว|นอกจากนี้|ที่เหลือ|ส่วนที่เหลือ|เคย|ในอดีต")
SUBSET = re.compile(r"ยาเม็ด|ยาฉีด|ยาน้ำ|แคปซูล|ครีม|ขี้ผึ้ง|เจล|ยาหยอด|ยาพ่น|ยาสูด|ยาเหน็บ|ผง|สารละลาย|ยาทา|ชนิดรับประทาน|"
                    r"ชนิดฉีด|รูปแบบ|บริษัท|ผู้ผลิต|ผู้รับอนุญาต|ผู้นำเข้า|\d\s*(?:mg|MG|มก|ml|มล)|ยาเดี่ยว|สูตรผสม|ยาผสม|ตำรับเดี่ยว")
DISPLAY_L = re.compile(r"(แสดง|เพียง|ด้านล่าง|ข้างต้น|ตัวอย่าง|เช่น|ในตาราง|ตารางนี้|ไม่เกิน)\s*(รายละเอียด)?(ทะเบียน|ใบอนุญาต)?\s*$")
DISPLAY_R = re.compile(r"^\s*(ที่แสดง|ข้างต้น|ด้านล่าง|ในตาราง|แรก)")
CANC_L = re.compile(r"(ถูก)?ยกเลิก(แล้ว)?\s*$|ที่(ถูก)?ยกเลิก(แล้ว)?\s*$|เพิกถอน(แล้ว)?\s*$")
CANC_R = re.compile(r"^\s*(ที่)?(ถูก)?(ยกเลิก|เพิกถอน)")
VALID_L = re.compile(r"(ยังใช้ได้|ใช้ได้อยู่|ใช้ได้|ยังมีผล(อยู่|ใช้ได้|บังคับใช้)?|มีผลบังคับใช้|ยังใช้งานได้|คงอยู่)\s*(\(valid\))?\s*$")
VALID_R = re.compile(r"^\s*(ที่)?(ยัง)?(ใช้ได้|มีผล|ใช้งานได้|คงอยู่)")
UNK_R = re.compile(r"^\s*มีสถานะ\s*[“\"]?\s*รอตรวจสอบสถานะ")
TOTAL_L = re.compile(r"(ทั้งหมด|รวม|\d\s*จาก)\s*$")
RELATIVE_L = re.compile(r"อีก\s*$")
ALL_VALID = re.compile(r"ยังใช้ได้ทั้งหมด|ทั้งหมด\S{0,15}?(ยังใช้ได้|ยังมีผล|คงอยู่)|ไม่มี\S{0,15}?(ที่)?(ถูก)?ยกเลิก")
ALL_CANC = re.compile(r"ทั้งหมด\s*\d[\d,]*\s*" + UNIT + r"\s*(ถูก)?ยกเลิก|ยกเลิก(แล้ว)?ทั้งหมด|ไม่มี\S{0,25}?ที่ยัง(มีผล|ใช้ได้|ใช้งาน)")
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _licish(ln, a):
    left = ln[max(0, a - LEFT_WIN):a]
    if NOT_LICENSE.search(left):
        return False
    return bool(LICENSE.search(left))


def _role(ln, a, b):
    left, right = ln[max(0, a - 25):a], ln[b:b + 30]
    if DISPLAY_L.search(left) or DISPLAY_R.match(right):
        return "display"
    if UNK_R.match(right):
        return "unknown"
    if RELATIVE_L.search(left):
        return "relative"
    if CANC_L.search(left):
        return "cancelled"
    if VALID_L.search(left):
        return "valid"
    if TOTAL_L.search(left):
        return "total"
    if CANC_R.match(right):
        return "cancelled_after"  # 「ทั้งหมด 37 รายการถูกยกเลิกแล้ว」：數字是總數、句子說全部註銷（前提檢查處理）
    if VALID_R.match(right):
        return "valid"
    return "plain"


def _want(role, f, explicit):
    """(可接受的值, 改寫用的值)"""
    t, v, c, u = f.get("total"), f.get("valid"), f.get("cancelled"), f.get("unknown") or 0
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role == "unknown":
        return {u}, u
    if role in ("total", "cancelled_after"):
        return {t}, t
    # plain：沒有限定詞
    return ({t}, t) if explicit else ({t, v}, t if t == v else None)


def _premise_ok(ln, f):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if ALL_VALID.search(ln) and v != t:
        return False
    if ALL_CANC.search(ln) and v:
        return False
    return True


def rewrite_line(ln, f, protect=()):
    """回傳 (新行, 跳過理由或 None)。"""
    hits = []
    for m in NUM.finditer(ln):
        role = _role(ln, m.start(), m.end())
        # 許可證字樣在左邊窗口內；或緊接在上一個許可證數字之後（「ใบอนุญาตทั้งหมด 155 ฉบับ ยังมีผลใช้ได้ 36 ฉบับ และถูกยกเลิกแล้ว 119 ฉบับ」）
        chained = bool(hits) and m.start() - hits[-1][0].end() <= 40 and role in ("valid", "cancelled", "unknown", "total", "cancelled_after") \
            and not NOT_LICENSE.search(ln[hits[-1][0].end():m.start()])
        if not (_licish(ln, m.start()) or chained):
            continue
        hits.append((m, role))
    if not hits:
        return ln, None
    roles = [r for _, r in hits if r != "display"]
    if not roles:
        return ln, None
    if any(r == "relative" for r in roles):
        return ln, "hedged/subset"
    for m, r in hits:
        if r == "display":
            continue
        win = ln[max(0, m.start() - 25):m.start()]
        if HEDGED.search(win) or SUBSET.search(win):
            return ln, "hedged/subset"
    explicit = any(r in ("valid", "cancelled", "unknown") for r in roles)
    spans = []
    for p in protect:
        i = ln.find(p)
        while i >= 0:
            spans.append((i, i + len(p)))
            i = ln.find(p, i + 1)
    subs = []
    for m, role in hits:
        if role == "display":
            continue
        old = int(m.group(1).replace(",", ""))
        ok, v = _want(role, f, explicit)
        if None in ok and len(ok) == 1:
            return ln, "no-fact"
        if old in ok:
            continue
        if v is None:
            return ln, "ambiguous"
        if old == 0:
            return ln, "zero-premise"
        if v == 0:
            return ln, "to-zero"
        if any(a <= m.start(1) < b for a, b in spans):
            return ln, "protected"
        subs.append((m, v))
    if not _premise_ok(ln, f):
        return ln, "premise"
    if not subs:
        return ln, None
    out, pos = [], 0
    for m, v in subs:
        out.append(ln[pos:m.start(1)])
        out.append(f"{v:,}" if "," in m.group(1) else str(v))
        pos = m.end(1)
    out.append(ln[pos:])
    return "".join(out), None


def rewrite(text, facts, protect=()):
    """text：整頁 markdown；facts：快照的 facts。回傳 (新內容, skipped [(理由, 行)])。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = []
    for ln in body.split("\n"):
        if "\x00" in ln or ln.startswith(("|", "#", ">", "<!--")) or not ln.strip():
            lines.append(ln)
            continue
        nl, why = rewrite_line(ln, facts, protect)
        if why:
            skipped.append((why, ln.strip()))
            nl = ln
        lines.append(nl)
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
