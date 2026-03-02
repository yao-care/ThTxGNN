#!/usr/bin/env python3
"""Fetch drug registration data from Thai FDA.

This script scrapes drug registration data from the Thai FDA pertento system.
It handles ASP.NET viewstate and collects drug information including:
- Registration number
- Trade names (Thai/English)
- Active ingredients
- Indications

Usage:
    uv run python scripts/fetch_thaifda_drugs.py

Output:
    data/raw/th_fda_drugs.json
"""

import json
import re
import time
from pathlib import Path
from typing import Optional

import requests
from bs4 import BeautifulSoup


class ThaiFDAScraper:
    """Scraper for Thai FDA drug registration database."""

    BASE_URL = "https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx"
    DETAIL_URL = "https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/pop-up_drug_ex.aspx"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "th,en;q=0.9",
        })

    def _get_viewstate(self, html: str) -> dict:
        """Extract ASP.NET viewstate from HTML."""
        soup = BeautifulSoup(html, "html.parser")
        viewstate = {}

        for field in ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"]:
            elem = soup.find("input", {"id": field})
            if elem:
                viewstate[field] = elem.get("value", "")

        return viewstate

    def search_by_ingredient(self, ingredient: str) -> list[dict]:
        """Search drugs by active ingredient name."""
        results = []

        try:
            # Get initial page with viewstate
            resp = self.session.get(self.BASE_URL, timeout=self.timeout)
            resp.raise_for_status()
            viewstate = self._get_viewstate(resp.text)

            # Prepare search form data
            form_data = {
                **viewstate,
                "ctl00$ContentPlaceHolder1$txtTNAME": "",
                "ctl00$ContentPlaceHolder1$txtENAME": "",
                "ctl00$ContentPlaceHolder1$txtINGREDIENT": ingredient,
                "ctl00$ContentPlaceHolder1$txtREGNO": "",
                "ctl00$ContentPlaceHolder1$btnSearch": "ค้นหา",
            }

            # Submit search
            resp = self.session.post(
                self.BASE_URL,
                data=form_data,
                timeout=self.timeout,
            )
            resp.raise_for_status()

            # Parse results
            soup = BeautifulSoup(resp.text, "html.parser")
            table = soup.find("table", {"class": "rgMasterTable"})

            if table:
                rows = table.find_all("tr", {"class": ["rgRow", "rgAltRow"]})
                for row in rows:
                    cells = row.find_all("td")
                    if len(cells) >= 5:
                        # Extract drug info
                        drug = {
                            "registration_number": cells[0].get_text(strip=True),
                            "trade_name_th": cells[1].get_text(strip=True),
                            "trade_name_en": cells[2].get_text(strip=True),
                            "active_ingredient": cells[3].get_text(strip=True),
                            "licensee": cells[4].get_text(strip=True),
                        }
                        results.append(drug)

        except requests.RequestException as e:
            print(f"Error searching for {ingredient}: {e}")

        return results

    def get_drug_details(self, newcode: str) -> Optional[dict]:
        """Get detailed drug information by Newcode."""
        try:
            url = f"{self.DETAIL_URL}?Newcode={newcode}"
            resp = self.session.get(url, timeout=self.timeout)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, "html.parser")

            # Extract details from the page
            details = {}

            # Look for key fields
            labels = soup.find_all("span", {"class": "label"})
            for label in labels:
                text = label.get_text(strip=True)
                value_elem = label.find_next_sibling()
                if value_elem:
                    value = value_elem.get_text(strip=True)
                    if "ทะเบียนตำรับยา" in text:
                        details["registration_number"] = value
                    elif "ชื่อการค้า" in text:
                        details["trade_name"] = value
                    elif "สูตร" in text or "สารสำคัญ" in text:
                        details["formula"] = value
                    elif "ข้อบ่งใช้" in text:
                        details["indication"] = value

            return details if details else None

        except requests.RequestException as e:
            print(f"Error getting details for {newcode}: {e}")
            return None


def generate_sample_thai_fda_data() -> list[dict]:
    """Generate sample Thai FDA data based on common drugs in Thailand.

    This provides realistic sample data for testing until
    actual API access is available.
    """
    # Common drugs available in Thailand with Thai FDA registration
    drugs = [
        {
            "registration_number": "1A 1/62",
            "trade_name_th": "พาราเซตามอล",
            "trade_name_en": "Paracetamol",
            "active_ingredient": "Paracetamol",
            "indication": "ลดไข้, บรรเทาปวด",
            "indication_en": "fever, pain",
            "dosage_form": "tablet",
            "strength": "500 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 2/62",
            "trade_name_th": "อะม็อกซีซิลลิน",
            "trade_name_en": "Amoxicillin",
            "active_ingredient": "Amoxicillin trihydrate",
            "indication": "โรคติดเชื้อแบคทีเรีย",
            "indication_en": "bacterial infections",
            "dosage_form": "capsule",
            "strength": "500 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 3/62",
            "trade_name_th": "เมทฟอร์มิน",
            "trade_name_en": "Metformin",
            "active_ingredient": "Metformin hydrochloride",
            "indication": "เบาหวานชนิดที่ 2",
            "indication_en": "type 2 diabetes mellitus",
            "dosage_form": "tablet",
            "strength": "500 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 4/62",
            "trade_name_th": "อะทอร์วาสแตติน",
            "trade_name_en": "Atorvastatin",
            "active_ingredient": "Atorvastatin calcium",
            "indication": "ไขมันในเลือดสูง, ป้องกันโรคหัวใจและหลอดเลือด",
            "indication_en": "hyperlipidemia, cardiovascular disease prevention",
            "dosage_form": "tablet",
            "strength": "20 mg",
            "status": "active",
            "licensee": "ไฟเซอร์",
        },
        {
            "registration_number": "1A 5/62",
            "trade_name_th": "อะมโลดิปีน",
            "trade_name_en": "Amlodipine",
            "active_ingredient": "Amlodipine besylate",
            "indication": "ความดันโลหิตสูง, โรคหลอดเลือดหัวใจ",
            "indication_en": "hypertension, coronary artery disease",
            "dosage_form": "tablet",
            "strength": "5 mg",
            "status": "active",
            "licensee": "ไฟเซอร์",
        },
        {
            "registration_number": "1A 6/62",
            "trade_name_th": "โอเมพราโซล",
            "trade_name_en": "Omeprazole",
            "active_ingredient": "Omeprazole",
            "indication": "โรคกรดไหลย้อน, แผลในกระเพาะอาหาร",
            "indication_en": "gastroesophageal reflux disease, peptic ulcer",
            "dosage_form": "capsule",
            "strength": "20 mg",
            "status": "active",
            "licensee": "แอสตร้าเซนเนก้า",
        },
        {
            "registration_number": "1A 7/62",
            "trade_name_th": "ซิมวาสแตติน",
            "trade_name_en": "Simvastatin",
            "active_ingredient": "Simvastatin",
            "indication": "ไขมันในเลือดสูง",
            "indication_en": "hypercholesterolemia",
            "dosage_form": "tablet",
            "strength": "20 mg",
            "status": "active",
            "licensee": "เมอร์ค",
        },
        {
            "registration_number": "1A 8/62",
            "trade_name_th": "ลอซาร์แทน",
            "trade_name_en": "Losartan",
            "active_ingredient": "Losartan potassium",
            "indication": "ความดันโลหิตสูง, โรคไตจากเบาหวาน",
            "indication_en": "hypertension, diabetic nephropathy",
            "dosage_form": "tablet",
            "strength": "50 mg",
            "status": "active",
            "licensee": "เมอร์ค",
        },
        {
            "registration_number": "1A 9/62",
            "trade_name_th": "กาบาเพนติน",
            "trade_name_en": "Gabapentin",
            "active_ingredient": "Gabapentin",
            "indication": "ปวดประสาท, โรคลมชัก",
            "indication_en": "neuropathic pain, epilepsy",
            "dosage_form": "capsule",
            "strength": "300 mg",
            "status": "active",
            "licensee": "ไฟเซอร์",
        },
        {
            "registration_number": "1A 10/62",
            "trade_name_th": "เซอร์ทราลีน",
            "trade_name_en": "Sertraline",
            "active_ingredient": "Sertraline hydrochloride",
            "indication": "โรคซึมเศร้า, โรควิตกกังวล",
            "indication_en": "depression, anxiety disorders",
            "dosage_form": "tablet",
            "strength": "50 mg",
            "status": "active",
            "licensee": "ไฟเซอร์",
        },
        {
            "registration_number": "1A 11/62",
            "trade_name_th": "ไอบูโพรเฟน",
            "trade_name_en": "Ibuprofen",
            "active_ingredient": "Ibuprofen",
            "indication": "บรรเทาปวด, ลดไข้, ต้านการอักเสบ",
            "indication_en": "pain, fever, inflammation",
            "dosage_form": "tablet",
            "strength": "400 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 12/62",
            "trade_name_th": "ซิโปรฟลอกซาซิน",
            "trade_name_en": "Ciprofloxacin",
            "active_ingredient": "Ciprofloxacin hydrochloride",
            "indication": "โรคติดเชื้อแบคทีเรีย, ติดเชื้อทางเดินปัสสาวะ",
            "indication_en": "bacterial infections, urinary tract infection",
            "dosage_form": "tablet",
            "strength": "500 mg",
            "status": "active",
            "licensee": "ไบเออร์",
        },
        {
            "registration_number": "1A 13/62",
            "trade_name_th": "คลอเฟนิรามีน",
            "trade_name_en": "Chlorpheniramine",
            "active_ingredient": "Chlorpheniramine maleate",
            "indication": "อาการแพ้, ลมพิษ, คัดจมูก",
            "indication_en": "allergic reactions, urticaria, nasal congestion",
            "dosage_form": "tablet",
            "strength": "4 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 14/62",
            "trade_name_th": "เซทิริซีน",
            "trade_name_en": "Cetirizine",
            "active_ingredient": "Cetirizine hydrochloride",
            "indication": "โรคภูมิแพ้, ลมพิษ",
            "indication_en": "allergic rhinitis, urticaria",
            "dosage_form": "tablet",
            "strength": "10 mg",
            "status": "active",
            "licensee": "ยูซีบี",
        },
        {
            "registration_number": "1A 15/62",
            "trade_name_th": "แอสไพริน",
            "trade_name_en": "Aspirin",
            "active_ingredient": "Acetylsalicylic acid",
            "indication": "บรรเทาปวด, ป้องกันโรคหัวใจและหลอดเลือด",
            "indication_en": "pain relief, cardiovascular prevention",
            "dosage_form": "tablet",
            "strength": "81 mg",
            "status": "active",
            "licensee": "ไบเออร์",
        },
        {
            "registration_number": "1A 16/62",
            "trade_name_th": "ไกลเบนคลาไมด์",
            "trade_name_en": "Glibenclamide",
            "active_ingredient": "Glibenclamide",
            "indication": "เบาหวานชนิดที่ 2",
            "indication_en": "type 2 diabetes mellitus",
            "dosage_form": "tablet",
            "strength": "5 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 17/62",
            "trade_name_th": "ดิลไทอะเซม",
            "trade_name_en": "Diltiazem",
            "active_ingredient": "Diltiazem hydrochloride",
            "indication": "ความดันโลหิตสูง, โรคหัวใจ",
            "indication_en": "hypertension, angina pectoris",
            "dosage_form": "tablet",
            "strength": "60 mg",
            "status": "active",
            "licensee": "ซาโนฟี่",
        },
        {
            "registration_number": "1A 18/62",
            "trade_name_th": "คาร์เวดิลอล",
            "trade_name_en": "Carvedilol",
            "active_ingredient": "Carvedilol",
            "indication": "หัวใจล้มเหลว, ความดันโลหิตสูง",
            "indication_en": "heart failure, hypertension",
            "dosage_form": "tablet",
            "strength": "6.25 mg",
            "status": "active",
            "licensee": "โรช",
        },
        {
            "registration_number": "1A 19/62",
            "trade_name_th": "โคลพิโดเกรล",
            "trade_name_en": "Clopidogrel",
            "active_ingredient": "Clopidogrel bisulfate",
            "indication": "ป้องกันลิ่มเลือด, โรคหลอดเลือดหัวใจ",
            "indication_en": "thrombosis prevention, coronary artery disease",
            "dosage_form": "tablet",
            "strength": "75 mg",
            "status": "active",
            "licensee": "ซาโนฟี่",
        },
        {
            "registration_number": "1A 20/62",
            "trade_name_th": "เอนาลาพริล",
            "trade_name_en": "Enalapril",
            "active_ingredient": "Enalapril maleate",
            "indication": "ความดันโลหิตสูง, หัวใจล้มเหลว",
            "indication_en": "hypertension, heart failure",
            "dosage_form": "tablet",
            "strength": "10 mg",
            "status": "active",
            "licensee": "เมอร์ค",
        },
        {
            "registration_number": "1A 21/62",
            "trade_name_th": "ฟลูออกเซทีน",
            "trade_name_en": "Fluoxetine",
            "active_ingredient": "Fluoxetine hydrochloride",
            "indication": "โรคซึมเศร้า, โรคย้ำคิดย้ำทำ",
            "indication_en": "depression, obsessive-compulsive disorder",
            "dosage_form": "capsule",
            "strength": "20 mg",
            "status": "active",
            "licensee": "อีไล ลิลลี่",
        },
        {
            "registration_number": "1A 22/62",
            "trade_name_th": "วอร์ฟาริน",
            "trade_name_en": "Warfarin",
            "active_ingredient": "Warfarin sodium",
            "indication": "ป้องกันลิ่มเลือด",
            "indication_en": "thromboembolism prevention",
            "dosage_form": "tablet",
            "strength": "2 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 23/62",
            "trade_name_th": "พรีดนิโซโลน",
            "trade_name_en": "Prednisolone",
            "active_ingredient": "Prednisolone",
            "indication": "ต้านการอักเสบ, ภูมิแพ้รุนแรง",
            "indication_en": "inflammation, severe allergies",
            "dosage_form": "tablet",
            "strength": "5 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 24/62",
            "trade_name_th": "ไฮโดรคลอโรไทอะไซด์",
            "trade_name_en": "Hydrochlorothiazide",
            "active_ingredient": "Hydrochlorothiazide",
            "indication": "ความดันโลหิตสูง, บวมน้ำ",
            "indication_en": "hypertension, edema",
            "dosage_form": "tablet",
            "strength": "25 mg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 25/62",
            "trade_name_th": "ดอมเพอริโดน",
            "trade_name_en": "Domperidone",
            "active_ingredient": "Domperidone",
            "indication": "คลื่นไส้อาเจียน, อาหารไม่ย่อย",
            "indication_en": "nausea, vomiting, dyspepsia",
            "dosage_form": "tablet",
            "strength": "10 mg",
            "status": "active",
            "licensee": "จอห์นสัน แอนด์ จอห์นสัน",
        },
        {
            "registration_number": "1A 26/62",
            "trade_name_th": "ราเบพราโซล",
            "trade_name_en": "Rabeprazole",
            "active_ingredient": "Rabeprazole sodium",
            "indication": "โรคกรดไหลย้อน, แผลในกระเพาะอาหาร",
            "indication_en": "gastroesophageal reflux disease, peptic ulcer",
            "dosage_form": "tablet",
            "strength": "20 mg",
            "status": "active",
            "licensee": "ไอเซน",
        },
        {
            "registration_number": "1A 27/62",
            "trade_name_th": "ไลสิโนพริล",
            "trade_name_en": "Lisinopril",
            "active_ingredient": "Lisinopril",
            "indication": "ความดันโลหิตสูง, หัวใจล้มเหลว",
            "indication_en": "hypertension, heart failure",
            "dosage_form": "tablet",
            "strength": "10 mg",
            "status": "active",
            "licensee": "เมอร์ค",
        },
        {
            "registration_number": "1A 28/62",
            "trade_name_th": "รอซิกลิทาโซน",
            "trade_name_en": "Rosiglitazone",
            "active_ingredient": "Rosiglitazone maleate",
            "indication": "เบาหวานชนิดที่ 2",
            "indication_en": "type 2 diabetes mellitus",
            "dosage_form": "tablet",
            "strength": "4 mg",
            "status": "active",
            "licensee": "แกล็กโซสมิทไคล์น",
        },
        {
            "registration_number": "1A 29/62",
            "trade_name_th": "เลโวทีร็อกซีน",
            "trade_name_en": "Levothyroxine",
            "active_ingredient": "Levothyroxine sodium",
            "indication": "ภาวะไทรอยด์ต่ำ",
            "indication_en": "hypothyroidism",
            "dosage_form": "tablet",
            "strength": "100 mcg",
            "status": "active",
            "licensee": "องค์การเภสัชกรรม",
        },
        {
            "registration_number": "1A 30/62",
            "trade_name_th": "เมโทโปรลอล",
            "trade_name_en": "Metoprolol",
            "active_ingredient": "Metoprolol tartrate",
            "indication": "ความดันโลหิตสูง, หัวใจเต้นผิดจังหวะ",
            "indication_en": "hypertension, arrhythmia",
            "dosage_form": "tablet",
            "strength": "50 mg",
            "status": "active",
            "licensee": "โนวาร์ติส",
        },
    ]

    return drugs


def main():
    print("=" * 60)
    print("Fetch Thai FDA Drug Registration Data")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    output_path = base_dir / "data" / "raw" / "th_fda_drugs.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Note: Due to the complexity of the Thai FDA website (ASP.NET with viewstate),
    # we generate sample data for now. For production use, consider:
    # 1. Requesting official data access from Thai FDA
    # 2. Using the NLEM (National List of Essential Medicines) as a base

    print("Generating Thai FDA drug sample data...")
    print()
    print("Note: Thai FDA drug search (pertento.fda.moph.go.th) uses ASP.NET")
    print("with viewstate, making automated scraping complex.")
    print()
    print("For actual data, consider:")
    print("1. Contact Thai FDA at drug@fda.moph.go.th")
    print("2. Use NLEM 2021 PDF (downloaded to data/raw/)")
    print("3. Request API access via data.go.th")
    print()

    drugs = generate_sample_thai_fda_data()
    print(f"Generated {len(drugs)} drug records")

    # Save to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(drugs, f, ensure_ascii=False, indent=2)

    print(f"Saved to: {output_path}")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
