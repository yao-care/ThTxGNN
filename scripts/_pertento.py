"""Thai FDA 公開查詢系統 pertento（FRM_SEARCH_DRUG.aspx）依成分查許可證（2026-10-31）。不用登入、沒有驗證碼。
ASP.NET WebForms：GET 取 __VIEWSTATE 等隱藏欄位 → POST 成分（txt_substance）＋查詢鈕 → RadGrid 預設每頁 20 筆（改成 100），
翻頁＝POST「Next Page」按鈕（rgPageNext）的 name。每列可見欄位：ลำดับ、เลขทะเบียน、ชื่อทางการค้าไทย、ชื่อทางการค้าอังกฤษ、
ชื่อผู้รับอนุญาต、ประเภทยาตามกฏหมาย、รูปแบบยาอังกฤษ、สถานะ（「คงอยู่」或「ยกเลิก(日期)」等原文）。
"""
import html
import re
import time

import requests

URL = "https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}
COLS = ("seq", "license_id", "brand_name_th", "brand_name_en", "license_holder", "legal_category", "dosage_form", "status")


def _form(h):
    """表單裡所有非按鈕欄位的現值（WebForms 翻頁要帶回整張表單，只帶 __VIEWSTATE 會回到第 1 頁）"""
    out = {}
    for tag in re.findall(r"<input[^>]*>", h):
        n = re.search(r'name="([^"]+)"', tag)
        if not n or 'type="submit"' in tag:
            continue
        v = re.search(r'value="([^"]*)"', tag)
        out[html.unescape(n.group(1))] = html.unescape(v.group(1)) if v else ""
    return out


def _cell(x):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", x)).replace("\xa0", " ").split())


def _rows(h):
    out = []
    for tr in re.findall(r'<tr class="rg(?:Row|AltRow)"[^>]*>(.*?)</tr>', h, re.S):
        tds = re.findall(r"<td([^>]*)>(.*?)</td>", tr, re.S)
        vis = [_cell(c) for a, c in tds if "display:none" not in a]
        hid = [_cell(c) for a, c in tds if "display:none" in a]
        if len(vis) >= 8:
            r = dict(zip(COLS, vis[:8]))
            r["newcode"] = hid[7] if len(hid) > 7 else ""  # 隱藏欄 Newcode_U：詳細頁 Public_Information_Drug?Newcode= 的參數
            out.append(r)
    return out


def _total(h):
    m = re.search(r"<strong>(\d+)</strong>\s*items in", h)
    return int(m.group(1)) if m else None


def _post(s, data):
    for attempt in range(4):
        try:
            r = s.post(URL, data=data, timeout=120)
            r.raise_for_status()
            return r.text
        except Exception:
            if attempt == 3:
                raise
            time.sleep(10 * (attempt + 1))


def search(substance, pause=1.0, max_pages=200):
    """回傳 (列, 網站顯示的總筆數)；查無資料時 ([], 0)"""
    s = requests.Session()
    s.headers.update(UA)
    h = s.get(URL, timeout=120).text
    f = _form(h)
    f.update({"ctl00$ContentPlaceHolder1$txt_substance": substance, "ctl00$ContentPlaceHolder1$btn_sea_drug": "ค้นหา"})
    h = _post(s, f)
    total = _total(h)
    rows = _rows(h)
    if total is None:
        return rows, len(rows)
    if total > len(rows):  # 每頁改 100 筆（RadGrid 的 PageSize 指令，同網頁上的每頁筆數下拉選單），翻頁次數少 5 倍
        f = _form(h)
        f.update({"__EVENTTARGET": "ctl00$ContentPlaceHolder1$RadGrid1",
                  "__EVENTARGUMENT": "FireCommand:ctl00$ContentPlaceHolder1$RadGrid1$ctl00;PageSize;100"})
        time.sleep(pause)
        h = _post(s, f)
        rows = _rows(h)
    for _ in range(max_pages):
        if len(rows) >= total:
            break
        nx = re.search(r'<input type="submit" name="([^"]+)"[^>]*class="rgPageNext"', h)
        if not nx:
            break
        f = _form(h)
        f[nx.group(1)] = " "
        time.sleep(pause)
        h = _post(s, f)
        got = _rows(h)
        if not got:
            break
        rows += got
    return rows, total


def status_of(text):
    """pertento 狀態原文 → valid／cancelled／unknown；認不得回傳 None。
    คงอยู่（有效）、ปลด SMP（解除上市後安全監視，屬有效）→ valid；ยกเลิก（註銷）、เพิกถอน（撤銷）、หมดอายุ（過期）、พักใช้（暫停）→ cancelled；
    รอตรวจสอบสถานะ（狀態待查核）→ unknown（不算有效）"""
    t = text.strip()
    if t.startswith(("คงอยู่", "ปลด SMP")):
        return "valid"
    if t.startswith(("ยกเลิก", "เพิกถอน", "หมดอายุ", "สิ้นอายุ", "พักใช้")):
        return "cancelled"
    if t.startswith("รอตรวจสอบสถานะ"):
        return "unknown"
    return None


HUMAN = re.compile(r"^\d[ABC]\b")  # 許可證號第二碼：A 人用國產、B 人用分裝、C 人用進口；D/E/F 獸用（G 以後是傳統藥）


def kind_of(license_id):
    """第一碼 1＝單方、2＝複方"""
    return "combo" if license_id.strip().startswith("2") else "single"


DETAIL = "https://pertento.fda.moph.go.th/FDA_INFORMATION_DRUG/SV_CENTER/GET_DATA_INFORMATION_DRUG"
PAGE = "https://pertento.fda.moph.go.th/FDA_INFORMATION_DRUG/Home/Public_Information_Drug?Newcode="


def detail_session():
    s = requests.Session()
    s.headers.update(UA)
    return s


def detail(s, newcode):
    """單張許可證詳細資料（詳細頁的 JSON 介面；要先開過詳細頁拿 cookie）：成分 XML_DRUG_FORMULA、狀態 STATUS_NAME、
    適應症 PRODUCT_INDICATION、獸用 XML_DRUG_ANIMAL 等。"""
    for attempt in range(4):
        try:
            if not s.cookies:
                s.get(PAGE + newcode, timeout=60)
            r = s.post(DETAIL, params={"Newcode": newcode}, data="", timeout=60,
                       headers={"Referer": PAGE + newcode, "Content-Type": "application/json;charset=utf-8"})
            r.raise_for_status()
            d = r.json()
            if d.get("MSG_CODE") == "403":
                s.cookies.clear()
                raise RuntimeError("403")
            return d
        except Exception:
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
