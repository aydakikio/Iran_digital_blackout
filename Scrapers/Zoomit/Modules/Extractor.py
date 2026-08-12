#libararies
from botasaurus.browser import Driver,cdp
from datetime import datetime,timezone
from collections import deque
from loguru import logger
import json

#Models
from Scrapers.Zoomit.Models.news_data import News

class Extractor:
    def __init__(self):
        self.captured_navigation_page_network_ids = []

    def listen_navigation_page(self, driver:Driver):
        self.clear_navigation_page_network_ids()
        driver.after_response_received(self._navigation_page_handler())

    def _navigation_page_handler(self):
        def after_response_handler(request_id, response, event):
            if "articles/browse" not in response.url:
                return
            if response.status != 200:
                return
            logger.info(f"✅ Captured: {response.url}")
            self.captured_navigation_page_network_ids.append(event.request_id)
        return after_response_handler

    def extract_navigation_articles_datetime(self, driver:Driver,pending_news:deque):
        if not self.captured_navigation_page_network_ids:
            logger.error("❌ No responses captured")
            return []
        body = driver.run_cdp_command(
            cdp.network.get_response_body(self.captured_navigation_page_network_ids[-1])
        )
        data = json.loads(body[0])

        self.clear_navigation_page_network_ids()

        for article in data.get("source", []):
            news_datetime=article.get("publishedDate")

            if self.in_range(news_datetime):
                news:News = News()

                news.published_time=news_datetime
                news.url=f'https://www.zoomit.ir/{article.get("slug")}'

                pending_news.append(news)
            else:
                logger.info("📰 News is out of range")


    def clear_navigation_page_network_ids(self):
        self.captured_navigation_page_network_ids.clear()

    @staticmethod
    def in_range(dt: datetime | str) -> bool:
        if isinstance(dt, str):
            dt = datetime.fromisoformat(dt.replace("Z", "+00:00"))
        return (
            datetime(2026, 2, 28, tzinfo=timezone.utc) <= dt <= datetime(2026, 5, 26, tzinfo=timezone.utc)
            # or -> For session 2
            # datetime(2026, 1, 8, tzinfo=timezone.utc) <= dt <= datetime(2026, 1, 30, tzinfo=timezone.utc)
        )

    