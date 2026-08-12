"""
Scraper of zoomit.ir

Shutdown ranges:
88 day shutdown -> start-> Feb 28 2026 | end -> May 22 2026
23 day shutdown -> start -> Jan 8 2026 | end -> Feb 2 2026

Iran  category:
https://www.zoomit.ir/archive?groupings=32319&sort=Newest&publishDate=All&readingTime=All&pageNumber=1
"""

#Libararies
from botasaurus.browser import browser, Driver,cdp
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
from collections import deque
from loguru import logger

#Models
from Models.news_data import News
from Models.user_data import Users

#Modules
from Modules.Extractor import Extractor

#global variables
pending_news:deque[News] = deque()
pending_users:deque[Users]

@browser(cache=False, reuse_driver=True,headless=False,wait_for_complete_page_load=True)
def zoomit_scraper(driver:Driver, data=None) -> int:
    global pending_news

    driver.enable_human_mode()
    driver.detect_and_bypass_cloudflare()
    driver.run_cdp_command(cdp.network.enable())

    logger.info("🌎 Browser successfully initialized")

    #init Extractor
    extractor:Extractor = Extractor()
    extractor.listen_navigation_page(driver)
    extractor.listen_comments(driver)
    logger.info("⚓ Listener hooks successfully inserted")

    #driver.get("https://www.zoomit.ir/archive?groupings=32319&sort=Newest&publishDate=All&readingTime=All&pageNumber=2", bypass_cloudflare=True)
    driver.get("https://www.zoomit.ir/tech-iran/408325-irancell-call-forwarding/", bypass_cloudflare=True)
    driver.long_random_sleep()

    #extractor.extract_navigation_articles_datetime(driver,pending_news)

    return 0

if __name__ == '__main__':
    zoomit_scraper()