"""Thai FDA and TCTR evidence collectors."""

import re
import time
from typing import Any
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup

from .base import BaseCollector, CollectorResult


class ThaiFDACollector(BaseCollector):
    """Collector for Thai FDA drug information.

    Data sources:
    - Thai FDA Drug Search: https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/
    - NDI (National Drug Information): https://ndi.fda.moph.go.th/
    """

    source_name = "thaifda"

    SEARCH_URL = "https://pertento.fda.moph.go.th/FDA_SEARCH_DRUG/SEARCH_DRUG/FRM_SEARCH_DRUG.aspx"
    NDI_URL = "https://ndi.fda.moph.go.th"

    def __init__(self, timeout: int = 30):
        """Initialize the Thai FDA collector.

        Args:
            timeout: Request timeout in seconds
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "th,en;q=0.9",
        })

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search Thai FDA for drug information.

        Args:
            drug: Drug name to search
            disease: Disease/indication (optional, for context)

        Returns:
            CollectorResult with drug registration information
        """
        query = {"drug": drug, "disease": disease}
        results = []

        try:
            # Search NDI for drug information
            ndi_results = self._search_ndi(drug)
            results.extend(ndi_results)

            # Search pertento FDA
            fda_results = self._search_pertento(drug)
            results.extend(fda_results)

            return self._make_result(
                query=query,
                data={
                    "drug": drug,
                    "disease": disease,
                    "registrations": results,
                    "count": len(results),
                    "sources": ["NDI", "Thai FDA Pertento"],
                },
                success=True,
            )

        except requests.RequestException as e:
            return self._make_result(
                query=query,
                data=None,
                success=False,
                error_message=f"Thai FDA request failed: {str(e)}",
            )
        except Exception as e:
            return self._make_result(
                query=query,
                data=None,
                success=False,
                error_message=f"Thai FDA search error: {str(e)}",
            )

    def _search_ndi(self, drug: str) -> list[dict]:
        """Search NDI (National Drug Information) database."""
        results = []

        try:
            # Search drug_info endpoint
            url = f"{self.NDI_URL}/drug_info"
            params = {"search": drug, "per_page": 20}

            resp = self.session.get(url, params=params, timeout=self.timeout)
            if resp.status_code != 200:
                return results

            soup = BeautifulSoup(resp.text, "html.parser")

            # Find drug entries with generic_name inputs
            forms = soup.find_all("form", {"id": "drug_info"})
            for form in forms:
                generic_input = form.find("input", {"name": "generic_name"})
                if generic_input:
                    generic_name = generic_input.get("value", "")

                    # Check if this matches our search
                    if drug.lower() in generic_name.lower():
                        # Find detail link
                        parent = form.find_parent("div")
                        detail_link = None
                        if parent:
                            link = parent.find("a", href=re.compile(r"drug_detail"))
                            if link:
                                detail_link = link.get("href", "")

                        results.append({
                            "source": "NDI",
                            "generic_name": generic_name,
                            "detail_url": detail_link,
                            "matched_query": drug,
                        })

        except Exception:
            pass  # Silently fail for individual search

        return results

    def _search_pertento(self, drug: str) -> list[dict]:
        """Search pertento.fda.moph.go.th drug database."""
        results = []

        try:
            # Get initial page to obtain viewstate
            resp = self.session.get(self.SEARCH_URL, timeout=self.timeout)
            if resp.status_code != 200:
                return results

            soup = BeautifulSoup(resp.text, "html.parser")

            # Extract ASP.NET viewstate
            viewstate = soup.find("input", {"id": "__VIEWSTATE"})
            viewstategenerator = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})
            eventvalidation = soup.find("input", {"id": "__EVENTVALIDATION"})

            if not viewstate or not eventvalidation:
                return results

            # Prepare search form data
            form_data = {
                "__VIEWSTATE": viewstate.get("value", ""),
                "__VIEWSTATEGENERATOR": viewstategenerator.get("value", "") if viewstategenerator else "",
                "__EVENTVALIDATION": eventvalidation.get("value", ""),
                "ctl00$ContentPlaceHolder1$txtTNAME": "",
                "ctl00$ContentPlaceHolder1$txtENAME": "",
                "ctl00$ContentPlaceHolder1$txtINGREDIENT": drug,
                "ctl00$ContentPlaceHolder1$txtREGNO": "",
                "ctl00$ContentPlaceHolder1$btnSearch": "ค้นหา",
            }

            # Submit search
            resp = self.session.post(
                self.SEARCH_URL,
                data=form_data,
                timeout=self.timeout,
            )

            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")

                # Look for result count
                result_info = soup.find(text=re.compile(r"พบ.*รายการ"))
                if result_info:
                    count_match = re.search(r"พบ\s*(\d+)\s*รายการ", str(result_info))
                    if count_match:
                        results.append({
                            "source": "Thai FDA Pertento",
                            "query": drug,
                            "result_count": int(count_match.group(1)),
                            "search_url": self.SEARCH_URL,
                        })

        except Exception:
            pass

        return results

    def get_drug_registration(self, registration_number: str) -> dict | None:
        """Get drug registration details by registration number.

        Args:
            registration_number: Thai FDA registration number (e.g., "1A 123/56")

        Returns:
            Drug registration details or None if not found
        """
        try:
            # Search by registration number
            resp = self.session.get(self.SEARCH_URL, timeout=self.timeout)
            if resp.status_code != 200:
                return None

            soup = BeautifulSoup(resp.text, "html.parser")

            viewstate = soup.find("input", {"id": "__VIEWSTATE"})
            viewstategenerator = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})
            eventvalidation = soup.find("input", {"id": "__EVENTVALIDATION"})

            if not viewstate or not eventvalidation:
                return None

            form_data = {
                "__VIEWSTATE": viewstate.get("value", ""),
                "__VIEWSTATEGENERATOR": viewstategenerator.get("value", "") if viewstategenerator else "",
                "__EVENTVALIDATION": eventvalidation.get("value", ""),
                "ctl00$ContentPlaceHolder1$txtTNAME": "",
                "ctl00$ContentPlaceHolder1$txtENAME": "",
                "ctl00$ContentPlaceHolder1$txtINGREDIENT": "",
                "ctl00$ContentPlaceHolder1$txtREGNO": registration_number,
                "ctl00$ContentPlaceHolder1$btnSearch": "ค้นหา",
            }

            resp = self.session.post(
                self.SEARCH_URL,
                data=form_data,
                timeout=self.timeout,
            )

            if resp.status_code == 200:
                return {
                    "registration_number": registration_number,
                    "source": "Thai FDA",
                    "search_performed": True,
                    "search_url": self.SEARCH_URL,
                }

        except Exception as e:
            return {
                "registration_number": registration_number,
                "source": "Thai FDA",
                "error": str(e),
            }

        return None


class TCTRCollector(BaseCollector):
    """Collector for Thai Clinical Trial Registry (TCTR).

    Data source: https://www.thaiclinicaltrials.org/

    TCTR is Thailand's official clinical trial registry, part of the
    WHO International Clinical Trials Registry Platform (ICTRP).
    """

    source_name = "tctr"

    BASE_URL = "https://www.thaiclinicaltrials.org"
    SEARCH_URL = "https://www.thaiclinicaltrials.org/show/search"
    API_URL = "https://www.thaiclinicaltrials.org/api/search"

    def __init__(self, timeout: int = 30):
        """Initialize the TCTR collector.

        Args:
            timeout: Request timeout in seconds
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "th,en;q=0.9",
        })

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search TCTR for clinical trials.

        Args:
            drug: Drug name to search
            disease: Disease/indication to search

        Returns:
            CollectorResult with clinical trial information
        """
        # Construct search query
        query_parts = [drug]
        if disease:
            query_parts.append(disease)
        search_query = " ".join(query_parts)

        query = {"drug": drug, "disease": disease, "search_query": search_query}
        trials = []

        try:
            # Try web scraping approach
            trials = self._search_web(search_query)

            return self._make_result(
                query=query,
                data={
                    "drug": drug,
                    "disease": disease,
                    "trials": trials,
                    "count": len(trials),
                    "source": "Thai Clinical Trial Registry",
                    "search_url": f"{self.SEARCH_URL}?q={quote(search_query)}",
                },
                success=True,
            )

        except requests.RequestException as e:
            return self._make_result(
                query=query,
                data=None,
                success=False,
                error_message=f"TCTR request failed: {str(e)}",
            )
        except Exception as e:
            return self._make_result(
                query=query,
                data=None,
                success=False,
                error_message=f"TCTR search error: {str(e)}",
            )

    def _search_web(self, query: str) -> list[dict]:
        """Search TCTR via web scraping."""
        trials = []

        try:
            # Search page
            url = f"{self.SEARCH_URL}"
            params = {
                "q": query,
                "type": "all",
            }

            resp = self.session.get(url, params=params, timeout=self.timeout)
            if resp.status_code != 200:
                return trials

            soup = BeautifulSoup(resp.text, "html.parser")

            # Find trial entries
            # TCTR typically shows results in a table or card format
            trial_elements = soup.find_all("div", class_=re.compile(r"trial|result|item", re.I))

            if not trial_elements:
                # Try finding table rows
                trial_elements = soup.find_all("tr", class_=re.compile(r"trial|result", re.I))

            for element in trial_elements[:20]:  # Limit to 20 results
                trial = self._parse_trial_element(element)
                if trial:
                    trials.append(trial)

            # If no structured results, look for TCTR IDs
            tctr_ids = re.findall(r"TCTR\d{14}", resp.text)
            for tctr_id in set(tctr_ids[:10]):  # Unique IDs, max 10
                if not any(t.get("tctr_id") == tctr_id for t in trials):
                    trials.append({
                        "tctr_id": tctr_id,
                        "source": "TCTR",
                        "detail_url": f"{self.BASE_URL}/show/{tctr_id}",
                    })

        except Exception:
            pass

        return trials

    def _parse_trial_element(self, element: Any) -> dict | None:
        """Parse a trial element from search results."""
        try:
            trial = {}

            # Look for TCTR ID
            text = element.get_text()
            tctr_match = re.search(r"(TCTR\d{14})", text)
            if tctr_match:
                trial["tctr_id"] = tctr_match.group(1)

            # Look for title
            title_elem = element.find(["h3", "h4", "a", "strong"])
            if title_elem:
                trial["title"] = title_elem.get_text(strip=True)[:200]

            # Look for status
            status_match = re.search(r"(Recruiting|Completed|Not yet recruiting|Terminated)", text, re.I)
            if status_match:
                trial["status"] = status_match.group(1)

            # Look for link
            link = element.find("a", href=True)
            if link:
                href = link.get("href", "")
                if href and not href.startswith("http"):
                    href = urljoin(self.BASE_URL, href)
                trial["url"] = href

            if trial.get("tctr_id") or trial.get("title"):
                trial["source"] = "TCTR"
                return trial

        except Exception:
            pass

        return None

    def get_trial_details(self, tctr_id: str) -> dict | None:
        """Get detailed information for a specific trial.

        Args:
            tctr_id: TCTR trial ID (e.g., "TCTR20240101001")

        Returns:
            Trial details or None if not found
        """
        try:
            url = f"{self.BASE_URL}/show/{tctr_id}"
            resp = self.session.get(url, timeout=self.timeout)

            if resp.status_code != 200:
                return None

            soup = BeautifulSoup(resp.text, "html.parser")

            trial = {
                "tctr_id": tctr_id,
                "url": url,
                "source": "TCTR",
            }

            # Extract key fields
            fields = {
                "title": ["Title", "ชื่อโครงการวิจัย"],
                "status": ["Status", "สถานะ"],
                "condition": ["Condition", "โรค/ภาวะ"],
                "intervention": ["Intervention", "การรักษา"],
                "sponsor": ["Sponsor", "ผู้สนับสนุน"],
                "start_date": ["Start Date", "วันที่เริ่มต้น"],
            }

            for key, labels in fields.items():
                for label in labels:
                    elem = soup.find(text=re.compile(label, re.I))
                    if elem:
                        parent = elem.find_parent(["tr", "div", "dt"])
                        if parent:
                            value_elem = parent.find_next(["td", "dd", "span"])
                            if value_elem:
                                trial[key] = value_elem.get_text(strip=True)[:500]
                                break

            return trial

        except Exception as e:
            return {
                "tctr_id": tctr_id,
                "error": str(e),
            }
