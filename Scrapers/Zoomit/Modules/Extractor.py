#libararies
from botasaurus.browser import Driver,cdp
from loguru import logger
import json

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

    def extract_navigation_articles_datetime(self, driver:Driver):
        if not self.captured_navigation_page_network_ids:
            logger.error("❌ No responses captured")
            return []
        body = driver.run_cdp_command(
            cdp.network.get_response_body(self.captured_navigation_page_network_ids[-1])
        )
        data = json.loads(body[0])

        self.clear_navigation_page_network_ids()

        for article in data.get("source", []):
            """
            articles.append({
                "slug": article.get("slug"),
                "publishedDate": article.get("publishedDate"),
            })
            """

            """Checks to see if it is in range or not if it is it addes that to queue"""

            print('artice_found:\n')
            print(article)
            print('\n')


    def clear_navigation_page_network_ids(self):
        self.captured_navigation_page_network_ids.clear()