"""RSS feed fetcher for health news monitoring."""

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import feedparser
import requests


@dataclass
class NewsArticle:
    """A news article from RSS feed."""

    title: str
    link: str
    source: str
    published: datetime | None = None
    summary: str = ""
    content: str = ""
    keywords_matched: list[str] = field(default_factory=list)
    article_id: str = ""

    def __post_init__(self):
        if not self.article_id:
            self.article_id = hashlib.md5(self.link.encode()).hexdigest()[:12]

    def to_dict(self) -> dict:
        return {
            "article_id": self.article_id,
            "title": self.title,
            "link": self.link,
            "source": self.source,
            "published": self.published.isoformat() if self.published else None,
            "summary": self.summary,
            "content": self.content[:1000] if self.content else "",
            "keywords_matched": self.keywords_matched,
        }


class RSSFetcher:
    """Fetcher for RSS feeds."""

    def __init__(self, keywords_path: str | Path | None = None, timeout: int = 30):
        """Initialize the RSS fetcher.

        Args:
            keywords_path: Path to keywords.json file
            timeout: Request timeout in seconds
        """
        self.timeout = timeout
        self.keywords = self._load_keywords(keywords_path)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "ThTxGNN Health News Monitor/1.0",
        })

    def _load_keywords(self, path: str | Path | None) -> dict:
        """Load keywords from JSON file."""
        if path is None:
            path = Path(__file__).parent.parent.parent / "data" / "news" / "keywords.json"

        path = Path(path)
        if path.exists():
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        return {"drugs": [], "diseases": [], "repurposing_patterns": []}

    def fetch_feed(self, feed_url: str, source_name: str = "") -> list[NewsArticle]:
        """Fetch and parse an RSS feed.

        Args:
            feed_url: URL of the RSS feed
            source_name: Name of the source for attribution

        Returns:
            List of NewsArticle objects
        """
        articles = []

        try:
            # Parse the feed
            feed = feedparser.parse(feed_url)

            if not source_name:
                source_name = feed.feed.get("title", feed_url)

            for entry in feed.entries:
                # Parse published date
                published = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    try:
                        published = datetime(*entry.published_parsed[:6])
                    except Exception:
                        pass
                elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                    try:
                        published = datetime(*entry.updated_parsed[:6])
                    except Exception:
                        pass

                # Get content
                content = ""
                if hasattr(entry, "content") and entry.content:
                    content = entry.content[0].get("value", "")
                elif hasattr(entry, "description"):
                    content = entry.description

                # Clean HTML from content
                content = re.sub(r"<[^>]+>", " ", content)
                content = re.sub(r"\s+", " ", content).strip()

                article = NewsArticle(
                    title=entry.get("title", ""),
                    link=entry.get("link", ""),
                    source=source_name,
                    published=published,
                    summary=entry.get("summary", "")[:500],
                    content=content[:2000],
                )

                # Check for keyword matches
                article.keywords_matched = self._find_keyword_matches(article)

                articles.append(article)

        except Exception as e:
            print(f"Error fetching {feed_url}: {e}")

        return articles

    def _find_keyword_matches(self, article: NewsArticle) -> list[str]:
        """Find matching keywords in article."""
        matches = []
        text = f"{article.title} {article.summary} {article.content}".lower()

        # Check drug keywords
        for drug in self.keywords.get("drugs", []):
            drug_name = drug.get("drug", "").lower()
            if drug_name and drug_name in text:
                matches.append(f"drug:{drug_name}")

            for term in drug.get("search_terms", []):
                if term.lower() in text:
                    matches.append(f"drug:{term}")
                    break

        # Check disease keywords
        for disease in self.keywords.get("diseases", []):
            disease_name = disease.get("disease", "").lower()
            if disease_name and disease_name in text:
                matches.append(f"disease:{disease_name}")

            for term in disease.get("search_terms", []):
                if term.lower() in text:
                    matches.append(f"disease:{term}")
                    break

        # Check repurposing patterns
        for pattern in self.keywords.get("repurposing_patterns", []):
            if pattern.lower() in text:
                matches.append(f"pattern:{pattern}")

        return list(set(matches))

    def fetch_all_feeds(self) -> list[NewsArticle]:
        """Fetch all configured news feeds."""
        all_articles = []

        # Get news sources from keywords
        sources = self.keywords.get("news_sources", [])

        for source in sources:
            if source.get("type") == "rss":
                articles = self.fetch_feed(
                    source.get("url", ""),
                    source.get("name", ""),
                )
                all_articles.extend(articles)

        return all_articles

    def filter_relevant_articles(
        self, articles: list[NewsArticle], min_matches: int = 1
    ) -> list[NewsArticle]:
        """Filter articles to only those with keyword matches.

        Args:
            articles: List of articles to filter
            min_matches: Minimum number of keyword matches required

        Returns:
            Filtered list of articles
        """
        return [a for a in articles if len(a.keywords_matched) >= min_matches]

    def save_articles(
        self, articles: list[NewsArticle], output_path: str | Path
    ) -> None:
        """Save articles to JSON file.

        Args:
            articles: List of articles to save
            output_path: Path to output JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "fetched_at": datetime.now().isoformat(),
            "count": len(articles),
            "articles": [a.to_dict() for a in articles],
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    """Main entry point for RSS fetching."""
    import argparse

    parser = argparse.ArgumentParser(description="Fetch health news via RSS")
    parser.add_argument(
        "--output",
        "-o",
        default="data/news/fetched_articles.json",
        help="Output JSON file path",
    )
    parser.add_argument(
        "--min-matches",
        "-m",
        type=int,
        default=1,
        help="Minimum keyword matches to include article",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Fetch Health News via RSS")
    print("=" * 60)

    fetcher = RSSFetcher()

    print("\n1. Fetching RSS feeds...")
    articles = fetcher.fetch_all_feeds()
    print(f"   Total articles: {len(articles)}")

    print("\n2. Filtering relevant articles...")
    relevant = fetcher.filter_relevant_articles(articles, args.min_matches)
    print(f"   Relevant articles: {len(relevant)}")

    print("\n3. Saving articles...")
    fetcher.save_articles(relevant, args.output)
    print(f"   Saved to: {args.output}")

    if relevant:
        print("\n4. Sample matches:")
        for article in relevant[:5]:
            print(f"   - {article.title[:60]}...")
            print(f"     Keywords: {', '.join(article.keywords_matched[:3])}")

    print("\nDone!")


if __name__ == "__main__":
    main()
