#libararies
from botasaurus.browser import Driver,cdp
from datetime import datetime,timezone
from bs4 import BeautifulSoup
from collections import deque
from loguru import logger
import json

#Models
from Scrapers.Zoomit.Models.news_data import News

class Extractor:
    def __init__(self):
        self.captured_news_ids = []
        self.captured_comment_ids = []
    
    #Network Traffic listeners
    def listen_navigation_page(self, driver:Driver):
        self.clear_news_ids()
        driver.after_response_received(self._navigation_page_handler())

    def listen_comments(self, driver):
        self.clear_comment_ids()
        driver.after_response_received(self._comment_handler())

    def _navigation_page_handler(self):
        def after_response_handler(request_id, response:cdp.network.Response, event:cdp.network.ResponseReceived):
            if "articles/browse" not in response.url:
                return
            if response.status != 200:
                return
            logger.info(f"✅ Captured: {response.url}")
            self.captured_news_ids.append(event.request_id)
        return after_response_handler

    def _comment_handler(self):
        def handler(request_id, response:cdp.network.Response, event:cdp.network.ResponseReceived):
            if response.mime_type != "application/json":
                return
            if "feedbacks" not in response.url:
                return
            if response.status != 200:
                logger.warning(f"⚠️ Failed {response.status}: {response.url}")
                return

            logger.info(f"✅ Comment captured: {response.url}")
            self.captured_comment_ids.append(event.request_id)

        return handler

    def extract_navigation_articles_datetime(self, driver:Driver,pending_news:deque):
        if not self.captured_news_ids:
            logger.error("❌ No responses captured")
            return []
        body = driver.run_cdp_command(
            cdp.network.get_response_body(self.captured_news_ids[-1])
        )
        data = json.loads(body[0])

        self.clear_news_ids()

        for article in data.get("source", []):
            news_datetime=article.get("publishedDate")

            if self.in_range(news_datetime):
                news:News = News()

                news.published_time=news_datetime
                news.url=f'https://www.zoomit.ir/{article.get("slug")}'

                pending_news.append(news)
            else:
                logger.info("📰 News is out of range")

    def extract_news(self, webpage_content:BeautifulSoup):
        print()

    def extract_comments(self, driver):
        if not self.captured_comment_ids:
            logger.error("❌ No comments captured")
            return []
        body = driver.run_cdp_command(
            cdp.network.get_response_body(self.captured_comment_ids[-1])
        )
        data = json.loads(body[0])
        self.clear_comment_ids()

        # Doing things on comment_datas

    def clear_news_ids(self):
        self.captured_news_ids.clear()

    def clear_comment_ids(self):
        self.captured_comment_ids.clear()
        
    
    @staticmethod
    def in_range(dt: datetime | str) -> bool:
        if isinstance(dt, str):
            dt = datetime.fromisoformat(dt.replace("Z", "+00:00"))
        return (
            datetime(2026, 2, 28, tzinfo=timezone.utc) <= dt <= datetime(2026, 5, 26, tzinfo=timezone.utc)
            # or -> For session 2
            # datetime(2026, 1, 8, tzinfo=timezone.utc) <= dt <= datetime(2026, 1, 30, tzinfo=timezone.utc)
        )
