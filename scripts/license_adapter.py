"""TH（Thai FDA 單張許可證頁）來源監看，給 license_refresh_20261029.py 用（2026-10-30）。

TH 站的本地資料是泰國國家基本藥物目錄整理出的 151 筆，每筆附 Thai FDA 的單張許可證頁（ndi.fda.moph.go.th/drug_detail…）。
Thai FDA 沒有可批次下載的註冊資料（資料目錄要登入、不開放註冊）。用戶 2026-10-30：改成固定抓、發現更新就開 issue。
做法：逐一抓證據包裡記載的 Thai FDA 許可證頁，去掉標籤與數字後算指紋；有頁面內容改變（例如狀態改成已撤銷）或打不開就列出來開 issue，
頁面不自動改。每頁間隔 1 秒。
"""
import base64
import hashlib
import json
import re
import time
from pathlib import Path

import requests

WATCH = True
RAW_FILE = "raw/thai_fda_page_watch.json"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}
REPO = Path(__file__).resolve().parents[1]


def _url(lic):
    """許可證號 → Thai FDA 許可證頁：rctype＝類別、rcno＝年份 2 碼＋流水號補到 5 碼、register＝許可證號原文的 base64
    （2026-10-30 依 data/raw/ndi_drug_list.json 的 39 個官方網址比對出規則，例 1A 358/64 → rcno=6400358）"""
    m = re.match(r"^(\w+) (\d+)/(\d{2})", lic)
    if not m:
        return None
    reg = base64.b64encode(lic.encode("utf-8")).decode("ascii")
    return f"https://ndi.fda.moph.go.th/drug_detail/index/?rctype={m.group(1)}&rcno={m.group(3)}{int(m.group(2)):05d}&register={reg}"


def _official():
    """data/raw/ndi_drug_list.json 裡的官方網址（register 參數有時多了 (NG) 等後綴，優先用官方的）"""
    f = REPO / "data/raw/ndi_drug_list.json"
    d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    return {x.get("registration_number"): str(x.get("url", "")).replace("\u00aeister", "&register") for x in d if x.get("url")}


def _urls():
    off = _official()
    out = set()
    for f in (REPO / "data/bundles").glob("*/drug_bundle.json"):
        b = json.loads(f.read_text(encoding="utf-8"))
        for r in ((b.get("thaifda") or {}).get("records") or []):
            lic = str(r.get("license_id") or "").strip()
            u = off.get(lic) or _url(lic)
            if u:
                out.add(u)
    return sorted(out)


def _fp(html):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\d+", "#", t)  # 日期、瀏覽數等數字不算變動
    t = " ".join(t.split())
    return hashlib.sha1(t.encode("utf-8")).hexdigest()[:16]


def fetch():
    urls = _urls()
    if not urls:
        raise RuntimeError("證據包與原始資料裡找不到 Thai FDA 許可證頁網址")
    out, fails = [], 0
    s = requests.Session()
    for u in urls:
        try:
            r = s.get(u, timeout=60, headers=UA)
            out.append({"url": u, "fp": _fp(r.text) if r.ok else f"HTTP {r.status_code}"})
        except Exception as e:
            fails += 1
            out.append({"url": u, "fp": "unreachable"})
        time.sleep(1)
    return out


def validate(new, old):
    bad = sum(1 for x in new if x["fp"] in ("unreachable",) or x["fp"].startswith("HTTP"))
    return [f"{bad}/{len(new)} 個 Thai FDA 頁打不開（網站可能擋連線或改版）"] if bad > 0.5 * len(new) else []


def describe(old, new):
    o = {x["url"]: x["fp"] for x in old}
    ch = [x["url"] for x in new if o.get(x["url"]) not in (None, x["fp"])]
    return f"{len(ch)} 個許可證頁內容有變：" + "、".join(ch[:20])


def status_index(new):
    return {}


def record_id(rec):
    return ""


def update(rec, new):
    return False
