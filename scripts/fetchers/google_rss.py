#!/usr/bin/env python3
"""
Google News RSS Fetcher - Thailand

ดึง RSS จากช่อง Google News สุขภาพ (ประเทศไทย), บันทึกลง data/news/google_rss.json
"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser

# ไดเรกทอรีหลักของโปรเจค
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News - ค้นหาข่าวสุขภาพและยา (ภาษาไทย)
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/search"
    "?q=%E0%B8%AA%E0%B8%B8%E0%B8%82%E0%B8%A0%E0%B8%B2%E0%B8%9E+%E0%B8%A2%E0%B8%B2"
    "&hl=th&gl=TH&ceid=TH:th"
)

# Google News - ค้นหาข่าวยารักษาโรค (เสริม)
GOOGLE_NEWS_DRUG_RSS = (
    "https://news.google.com/rss/search"
    "?q=%E0%B8%A2%E0%B8%B2%E0%B8%A3%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%B2+%E0%B9%82%E0%B8%A3%E0%B8%84"
    "&hl=th&gl=TH&ceid=TH:th"
)


def generate_id(title: str, link: str) -> str:
    """สร้าง ID ข่าว (hash จากชื่อเรื่องและลิงก์)"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def parse_source(entry) -> dict:
    """ดึงข้อมูลแหล่งข่าวจาก RSS entry"""
    source_name = "Google News"
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """แปลงวันที่เผยแพร่เป็นรูปแบบ ISO 8601"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """ทำความสะอาดข้อความสรุป (ลบ HTML tags ฯลฯ)"""
    import re
    clean = re.sub(r"<[^>]+>", "", summary)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_rss_feed(url: str, source_name: str) -> list[dict]:
    """ดึง RSS feed"""
    print(f"กำลังดึง {source_name}...")
    print(f"  URL: {url[:80]}...")

    feed = feedparser.parse(url)

    if feed.bozo:
        print(f"  คำเตือน: ปัญหาในการแปลง RSS - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"  พบ {len(news_items)} ข่าว")
    return news_items


def fetch_google_news_thailand() -> list[dict]:
    """ดึงข่าวสุขภาพจาก Google News ประเทศไทย"""
    all_news = []

    # ดึงข่าวสุขภาพ+ยา
    health_news = fetch_rss_feed(GOOGLE_NEWS_HEALTH_RSS, "Google News สุขภาพไทย")
    all_news.extend(health_news)

    # ดึงข่าวยารักษาโรค
    drug_news = fetch_rss_feed(GOOGLE_NEWS_DRUG_RSS, "Google News ยารักษาโรค")
    all_news.extend(drug_news)

    # ลบซ้ำตาม ID
    seen_ids = set()
    unique_news = []
    for item in all_news:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_news.append(item)

    return unique_news


def main():
    # ตรวจสอบว่าไดเรกทอรีมีอยู่
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # ดึงข่าว
    news_items = fetch_google_news_thailand()

    # ผลลัพธ์
    output = {
        "source": "google_rss_th",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(news_items),
        "news": news_items
    }

    output_path = DATA_DIR / "google_rss.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nผลลัพธ์: {output_path}")
    print(f"  - จำนวนข่าวทั้งหมด: {len(news_items)}")


if __name__ == "__main__":
    main()
