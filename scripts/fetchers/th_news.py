"""Thai health news fetcher for drug repurposing monitoring."""

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup

from .rss_fetcher import NewsArticle, RSSFetcher


class ThaiHealthNewsFetcher(RSSFetcher):
    """Fetcher specifically for Thai health news sources.

    Supports:
    - HFocus (hfocus.org) - Thai health news
    - Bangkok Post Health section
    - Thai PBS health news
    - Manager Online health section
    """

    # Thai health news sources
    SOURCES = {
        "hfocus": {
            "name": "HFocus",
            "rss": "https://www.hfocus.org/feed",
            "url": "https://www.hfocus.org",
            "language": "th",
        },
        "thairath_health": {
            "name": "Thairath Health",
            "url": "https://www.thairath.co.th/lifestyle/health",
            "language": "th",
            "type": "web",
        },
        "bangkokpost_health": {
            "name": "Bangkok Post Health",
            "url": "https://www.bangkokpost.com/thailand/general/health",
            "language": "en",
            "type": "web",
        },
        "manager_health": {
            "name": "Manager Health",
            "url": "https://mgronline.com/qol",
            "language": "th",
            "type": "web",
        },
    }

    def __init__(self, keywords_path: str | Path | None = None, timeout: int = 30):
        """Initialize the Thai health news fetcher.

        Args:
            keywords_path: Path to keywords.json file
            timeout: Request timeout in seconds
        """
        super().__init__(keywords_path, timeout)
        self.session.headers.update({
            "Accept-Language": "th,en;q=0.9",
        })

    def fetch_hfocus(self) -> list[NewsArticle]:
        """Fetch news from HFocus (Thai health policy news)."""
        articles = []

        try:
            # HFocus has RSS feed
            articles = self.fetch_feed(
                self.SOURCES["hfocus"]["rss"],
                self.SOURCES["hfocus"]["name"],
            )
        except Exception as e:
            print(f"Error fetching HFocus: {e}")

        return articles

    def fetch_bangkok_post_health(self) -> list[NewsArticle]:
        """Fetch health news from Bangkok Post."""
        articles = []

        try:
            url = self.SOURCES["bangkokpost_health"]["url"]
            resp = self.session.get(url, timeout=self.timeout)

            if resp.status_code != 200:
                return articles

            resp.encoding = resp.apparent_encoding or 'utf-8'
            soup = BeautifulSoup(resp.text, "html.parser")

            # Find article elements
            article_elements = soup.find_all("article") or soup.find_all(
                "div", class_=re.compile(r"article|news|story", re.I)
            )

            for elem in article_elements[:20]:
                try:
                    # Find title and link
                    title_elem = elem.find(["h2", "h3", "h4", "a"])
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    link = ""

                    if title_elem.name == "a":
                        link = title_elem.get("href", "")
                    else:
                        link_elem = elem.find("a", href=True)
                        if link_elem:
                            link = link_elem.get("href", "")

                    if not title or not link:
                        continue

                    # Make absolute URL
                    if link and not link.startswith("http"):
                        link = f"https://www.bangkokpost.com{link}"

                    # Find summary
                    summary_elem = elem.find(["p", "span"], class_=re.compile(r"summary|excerpt|desc", re.I))
                    summary = summary_elem.get_text(strip=True) if summary_elem else ""

                    article = NewsArticle(
                        title=title,
                        link=link,
                        source="Bangkok Post Health",
                        summary=summary[:500],
                    )
                    article.keywords_matched = self._find_keyword_matches(article)
                    articles.append(article)

                except Exception:
                    continue

        except Exception as e:
            print(f"Error fetching Bangkok Post: {e}")

        return articles

    def fetch_manager_health(self) -> list[NewsArticle]:
        """Fetch health news from Manager Online."""
        articles = []

        try:
            url = self.SOURCES["manager_health"]["url"]
            resp = self.session.get(url, timeout=self.timeout)

            if resp.status_code != 200:
                return articles

            # Ensure proper encoding for Thai content
            resp.encoding = resp.apparent_encoding or 'utf-8'
            soup = BeautifulSoup(resp.text, "html.parser")

            # Find news links
            links = soup.find_all("a", href=re.compile(r"/qol/.*"))

            seen_urls = set()
            for link in links[:30]:
                try:
                    href = link.get("href", "")
                    if not href or href in seen_urls:
                        continue

                    # Get title
                    title = link.get_text(strip=True)
                    if not title or len(title) < 10:
                        continue

                    # Make absolute URL
                    if not href.startswith("http"):
                        href = f"https://mgronline.com{href}"

                    seen_urls.add(href)

                    article = NewsArticle(
                        title=title,
                        link=href,
                        source="Manager Health",
                    )
                    article.keywords_matched = self._find_keyword_matches(article)
                    articles.append(article)

                except Exception:
                    continue

        except Exception as e:
            print(f"Error fetching Manager Online: {e}")

        return articles

    def fetch_thairath_health(self) -> list[NewsArticle]:
        """Fetch health news from Thairath."""
        articles = []

        try:
            url = self.SOURCES["thairath_health"]["url"]
            resp = self.session.get(url, timeout=self.timeout)

            if resp.status_code != 200:
                return articles

            resp.encoding = resp.apparent_encoding or 'utf-8'
            soup = BeautifulSoup(resp.text, "html.parser")

            # Find article cards
            cards = soup.find_all("div", class_=re.compile(r"card|article|item", re.I))

            for card in cards[:20]:
                try:
                    link_elem = card.find("a", href=True)
                    if not link_elem:
                        continue

                    href = link_elem.get("href", "")
                    title = link_elem.get_text(strip=True)

                    if not title or len(title) < 10:
                        title_elem = card.find(["h2", "h3", "h4"])
                        if title_elem:
                            title = title_elem.get_text(strip=True)

                    if not title or not href:
                        continue

                    if not href.startswith("http"):
                        href = f"https://www.thairath.co.th{href}"

                    article = NewsArticle(
                        title=title,
                        link=href,
                        source="Thairath Health",
                    )
                    article.keywords_matched = self._find_keyword_matches(article)
                    articles.append(article)

                except Exception:
                    continue

        except Exception as e:
            print(f"Error fetching Thairath: {e}")

        return articles

    def fetch_all_thai_sources(self) -> list[NewsArticle]:
        """Fetch news from all Thai health news sources."""
        all_articles = []

        print("  Fetching HFocus...")
        all_articles.extend(self.fetch_hfocus())

        print("  Fetching Bangkok Post Health...")
        all_articles.extend(self.fetch_bangkok_post_health())

        print("  Fetching Manager Health...")
        all_articles.extend(self.fetch_manager_health())

        print("  Fetching Thairath Health...")
        all_articles.extend(self.fetch_thairath_health())

        # Also fetch from configured RSS feeds
        print("  Fetching configured RSS feeds...")
        all_articles.extend(self.fetch_all_feeds())

        # Deduplicate by URL
        seen_urls = set()
        unique_articles = []
        for article in all_articles:
            if article.link not in seen_urls:
                seen_urls.add(article.link)
                unique_articles.append(article)

        return unique_articles

    def search_pubmed_news(self, query: str, max_results: int = 20) -> list[NewsArticle]:
        """Search PubMed for recent publications (as news source).

        Args:
            query: Search query
            max_results: Maximum number of results

        Returns:
            List of NewsArticle objects from PubMed
        """
        articles = []

        try:
            # PubMed E-utilities search
            search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            params = {
                "db": "pubmed",
                "term": f"{query} AND Thailand[Affiliation]",
                "retmax": max_results,
                "retmode": "json",
                "sort": "date",
            }

            resp = self.session.get(search_url, params=params, timeout=self.timeout)
            if resp.status_code != 200:
                return articles

            data = resp.json()
            pmids = data.get("esearchresult", {}).get("idlist", [])

            if not pmids:
                return articles

            # Fetch article summaries
            summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            params = {
                "db": "pubmed",
                "id": ",".join(pmids),
                "retmode": "json",
            }

            resp = self.session.get(summary_url, params=params, timeout=self.timeout)
            if resp.status_code != 200:
                return articles

            data = resp.json()
            results = data.get("result", {})

            for pmid in pmids:
                if pmid not in results:
                    continue

                info = results[pmid]
                title = info.get("title", "")
                pub_date = info.get("pubdate", "")

                article = NewsArticle(
                    title=title,
                    link=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    source="PubMed",
                    summary=f"Authors: {info.get('authors', [{}])[0].get('name', 'Unknown') if info.get('authors') else 'Unknown'}",
                )
                article.keywords_matched = self._find_keyword_matches(article)
                articles.append(article)

        except Exception as e:
            print(f"Error searching PubMed: {e}")

        return articles


def main():
    """Main entry point for Thai health news fetching."""
    import argparse

    parser = argparse.ArgumentParser(description="Fetch Thai health news")
    parser.add_argument(
        "--output",
        "-o",
        default="data/news/thai_news.json",
        help="Output JSON file path",
    )
    parser.add_argument(
        "--min-matches",
        "-m",
        type=int,
        default=0,
        help="Minimum keyword matches (0 = all articles)",
    )
    parser.add_argument(
        "--pubmed-query",
        "-p",
        default="drug repurposing",
        help="PubMed search query",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Fetch Thai Health News")
    print("=" * 60)

    fetcher = ThaiHealthNewsFetcher()

    print("\n1. Fetching Thai health news sources...")
    articles = fetcher.fetch_all_thai_sources()
    print(f"   Total articles: {len(articles)}")

    print("\n2. Searching PubMed...")
    pubmed_articles = fetcher.search_pubmed_news(args.pubmed_query)
    articles.extend(pubmed_articles)
    print(f"   PubMed articles: {len(pubmed_articles)}")

    if args.min_matches > 0:
        print(f"\n3. Filtering (min {args.min_matches} matches)...")
        articles = fetcher.filter_relevant_articles(articles, args.min_matches)
        print(f"   Filtered articles: {len(articles)}")

    print(f"\n4. Saving to {args.output}...")
    fetcher.save_articles(articles, args.output)

    # Show statistics
    sources = {}
    for article in articles:
        sources[article.source] = sources.get(article.source, 0) + 1

    print("\n5. Statistics by source:")
    for source, count in sorted(sources.items(), key=lambda x: -x[1]):
        print(f"   - {source}: {count}")

    if articles:
        print("\n6. Sample articles with keyword matches:")
        matched = [a for a in articles if a.keywords_matched]
        for article in matched[:5]:
            print(f"   - {article.title[:50]}...")
            print(f"     Source: {article.source}")
            print(f"     Keywords: {', '.join(article.keywords_matched[:3])}")

    print("\nDone!")


if __name__ == "__main__":
    main()
