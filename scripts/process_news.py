#!/usr/bin/env python3
"""
สคริปต์ประมวลผลข่าว ThTxGNN

ฟังก์ชัน:
1. อ่านไฟล์ข่าวจาก data/news/*.json
2. โหลด keywords.json สำหรับจับคู่คำสำคัญ
3. **กรองข่าวให้ต้องมีทั้งยาและโรค** (ไม่ใช่ยาหรือโรคอย่างเดียว)
4. ลบข่าวซ้ำข้ามแหล่ง
5. สร้าง news-index.json สำหรับ frontend
"""

import json
import re
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path

# โฟลเดอร์โปรเจค
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"
DOCS_DIR = PROJECT_ROOT / "docs"
NEWS_INDEX_PATH = DOCS_DIR / "data" / "news-index.json"

# การตั้งค่า
SIMILARITY_THRESHOLD = 0.8  # เกณฑ์ความคล้ายคลึงของหัวข้อ
TIME_WINDOW_HOURS = 24  # หน้าต่างเวลาสำหรับการลบซ้ำ (ชั่วโมง)
MAX_NEWS_AGE_DAYS = 30  # จำนวนวันสูงสุดที่เก็บข่าว


def load_json(path: Path) -> dict | list:
    """โหลดไฟล์ JSON"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict | list, path: Path):
    """บันทึกไฟล์ JSON"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_sources() -> list[dict]:
    """โหลดข่าวจากทุกแหล่ง"""
    all_news = []
    excluded = {"keywords.json", "synonyms.json", "synonyms.json.template"}

    for json_file in DATA_DIR.glob("*.json"):
        if json_file.name in excluded:
            continue

        try:
            data = load_json(json_file)
            source_name = data.get("source", json_file.stem)

            # รองรับทั้งรูปแบบ news และ articles
            news_items = data.get("news", data.get("articles", []))
            print(f"  - {json_file.name}: {len(news_items)} ข่าว")

            for item in news_items:
                item["_source_file"] = source_name
                all_news.append(item)

        except Exception as e:
            print(f"  คำเตือน: ไม่สามารถโหลด {json_file.name} - {e}")

    return all_news


def filter_old_news(news_items: list[dict]) -> list[dict]:
    """กรองข่าวเก่ากว่า 30 วัน"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_NEWS_AGE_DAYS)
    filtered = []

    for item in news_items:
        try:
            pub_str = item.get("published", "")
            if pub_str:
                published = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                if published >= cutoff:
                    filtered.append(item)
            else:
                # ไม่มีวันที่ ให้เก็บไว้
                filtered.append(item)
        except (ValueError, TypeError):
            filtered.append(item)

    removed = len(news_items) - len(filtered)
    if removed > 0:
        print(f"  กรองข่าวเก่า: {removed} ข่าว")

    return filtered


def title_similarity(title1: str, title2: str) -> float:
    """คำนวณความคล้ายคลึงของหัวข้อ"""
    clean1 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title1).strip()
    clean2 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title2).strip()
    return SequenceMatcher(None, clean1, clean2).ratio()


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """ลบข่าวซ้ำข้ามแหล่ง รวมแหล่งที่มาของข่าวคล้ายกัน"""
    sorted_news = sorted(
        news_items,
        key=lambda x: x.get("published") or "",
        reverse=True
    )

    merged = []
    used_indices = set()

    for i, item in enumerate(sorted_news):
        if i in used_indices:
            continue

        similar_items = [item]

        try:
            pub_str = item.get("published") or datetime.now(timezone.utc).isoformat()
            item_time = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            item_time = datetime.now(timezone.utc)

        for j, other in enumerate(sorted_news[i + 1:], start=i + 1):
            if j in used_indices:
                continue

            try:
                pub_str = other.get("published") or datetime.now(timezone.utc).isoformat()
                other_time = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
            except (ValueError, TypeError):
                other_time = datetime.now(timezone.utc)

            time_diff = abs((item_time - other_time).total_seconds() / 3600)

            if time_diff > TIME_WINDOW_HOURS:
                continue

            if title_similarity(item.get("title", ""), other.get("title", "")) >= SIMILARITY_THRESHOLD:
                similar_items.append(other)
                used_indices.add(j)

        # รวมแหล่งข่าว
        all_sources = []
        seen_links = set()
        for sim_item in similar_items:
            # รองรับทั้ง sources array และ single link/source
            sources = sim_item.get("sources", [])
            if not sources:
                link = sim_item.get("link", "")
                source_name = sim_item.get("source", sim_item.get("_source_file", "Unknown"))
                if link:
                    sources = [{"name": source_name, "link": link}]

            for source in sources:
                link = source.get("link", "")
                if link and link not in seen_links:
                    seen_links.add(link)
                    all_sources.append(source)

        # ใช้เวลาเผยแพร่ที่เร็วที่สุด
        try:
            pub_times = []
            for s in similar_items:
                pub_str = s.get("published")
                if pub_str:
                    pub_times.append(datetime.fromisoformat(pub_str.replace("Z", "+00:00")))
            earliest_time = min(pub_times) if pub_times else datetime.now(timezone.utc)
        except (ValueError, TypeError):
            earliest_time = datetime.now(timezone.utc)

        # สร้าง ID จาก title hash
        import hashlib
        news_id = hashlib.sha256(item.get("title", "").encode()).hexdigest()[:12]

        merged_item = {
            "id": item.get("id", news_id),
            "title": re.sub(r"\s*[-–—]\s*[^\s]+$", "", item.get("title", "")).strip(),
            "published": earliest_time.isoformat(),
            "summary": item.get("summary", ""),
            "sources": all_sources,
            "matched_keywords": []
        }
        merged.append(merged_item)
        used_indices.add(i)

    print(f"  หลังลบซ้ำ: {len(merged)} ข่าว (รวม {len(news_items) - len(merged)} ข่าว)")
    return merged


def match_keywords(news_items: list[dict], keywords: dict) -> list[dict]:
    """จับคู่คำสำคัญในข่าว"""
    drugs = keywords.get("drugs", [])
    indications = keywords.get("indications", [])

    # สร้างแผนที่ slug -> name ของยา
    drug_name_map = {d["slug"]: d["name"] for d in drugs}

    matched_count = 0

    for item in news_items:
        text_to_search = f"{item['title']} {item.get('summary', '')}".lower()
        matches = []

        # จับคู่ยา
        for drug in drugs:
            drug_name = drug["name"]
            drug_slug = drug["slug"]

            # คำสำคัญภาษาอังกฤษ
            for kw in drug["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "drug",
                        "slug": drug_slug,
                        "keyword": kw,
                        "name": drug_name,
                        "url": drug["url"]
                    })
                    break  # บันทึกเฉพาะ 1 ครั้งต่อยา

            # คำสำคัญภาษาไทย
            for kw in drug["keywords"].get("th", []):
                if kw in item["title"] or kw in item.get("summary", ""):
                    # หลีกเลี่ยงซ้ำ
                    if not any(m["slug"] == drug_slug for m in matches):
                        matches.append({
                            "type": "drug",
                            "slug": drug_slug,
                            "keyword": kw,
                            "name": drug_name,
                            "url": drug["url"]
                        })
                    break

        # จับคู่ข้อบ่งใช้
        for ind in indications:
            ind_name = ind["name"]

            # แปลง related_drugs จาก slug เป็น {slug, name}
            related_drugs = [
                {"slug": slug, "name": drug_name_map.get(slug, slug)}
                for slug in ind.get("related_drugs", [])
            ]

            # คำสำคัญภาษาอังกฤษ
            for kw in ind["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "indication",
                        "name": ind_name,
                        "keyword": kw,
                        "related_drugs": related_drugs
                    })
                    break

            # คำสำคัญภาษาไทย
            for kw in ind["keywords"].get("th", []):
                if kw in item["title"] or kw in item.get("summary", ""):
                    # หลีกเลี่ยงซ้ำ
                    if not any(m.get("keyword") == kw and m["type"] == "indication" for m in matches):
                        matches.append({
                            "type": "indication",
                            "name": ind_name,
                            "keyword": kw,
                            "related_drugs": related_drugs
                        })
                    break

        item["matched_keywords"] = matches
        if matches:
            matched_count += 1

    print(f"  จับคู่คำสำคัญ: {matched_count} ข่าว")
    return news_items


def generate_news_index(matched_news: list[dict]):
    """สร้างไฟล์ news-index.json สำหรับ frontend"""
    # เฉพาะข่าวที่มีทั้งยาและโรค
    indexed_news = [
        {
            "id": item["id"],
            "title": item["title"],
            "published": item["published"],
            "sources": item["sources"],
            "keywords": item["matched_keywords"]
        }
        for item in matched_news
        if item.get("matched_keywords")  # จะมีเฉพาะข่าวที่มีทั้งยาและโรค
    ]

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "count": len(indexed_news),
        "news": indexed_news
    }

    save_json(output, NEWS_INDEX_PATH)
    print(f"  สร้างดัชนี: {NEWS_INDEX_PATH}")
    print(f"  จำนวนข่าว: {len(indexed_news)}")


def main():
    print("=" * 60)
    print("ประมวลผลข่าวสุขภาพ ThTxGNN")
    print("=" * 60)
    print("\nหมายเหตุ: ข่าวต้องมีทั้งยาและโรคถึงจะแสดง")

    # 1. โหลดข่าวจากทุกแหล่ง
    print("\n1. โหลดไฟล์ข่าว:")
    all_news = load_all_sources()
    print(f"  รวม: {len(all_news)} ข่าว")

    if not all_news:
        print("\n  ไม่พบข่าว กรุณาเรียกใช้ fetcher ก่อน")
        return

    # 2. กรองข่าวเก่า
    print("\n2. กรองข่าวเก่า:")
    all_news = filter_old_news(all_news)

    # 3. ลบข่าวซ้ำ
    print("\n3. ลบข่าวซ้ำข้ามแหล่ง:")
    all_news = deduplicate_news(all_news)

    # 4. โหลด keywords และจับคู่
    print("\n4. จับคู่คำสำคัญ:")
    keywords_path = DATA_DIR / "keywords.json"
    if not keywords_path.exists():
        print(f"  ไม่พบ {keywords_path}")
        return

    keywords = load_json(keywords_path)
    print(f"  คำสำคัญ: {keywords.get('drug_count', 0)} ยา + {keywords.get('indication_count', 0)} ข้อบ่งใช้")
    all_news = match_keywords(all_news, keywords)

    # 5. สร้าง news-index.json
    print("\n5. สร้างดัชนีข่าว:")
    generate_news_index(all_news)

    # 6. แสดงตัวอย่าง
    matched = [n for n in all_news if n.get("matched_keywords")]
    if matched:
        print("\n6. ตัวอย่างข่าวที่ตรง:")
        for item in matched[:3]:
            print(f"   - {item['title'][:60]}...")
            drugs = [k["name"] for k in item["matched_keywords"] if k["type"] == "drug"]
            diseases = [k["name"] for k in item["matched_keywords"] if k["type"] == "indication"]
            print(f"     ยา: {', '.join(drugs[:3])}")
            print(f"     โรค: {', '.join(diseases[:3])}")

    print("\nเสร็จสิ้น!")


if __name__ == "__main__":
    main()
