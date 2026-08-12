"""
Scraper of zoomit.ir

Iran news category:
https://www.zoomit.ir/archive?groupings=32319&sort=Newest&publishDate=All&readingTime=All&pageNumber=1
"""

#Libararies
from botasaurus.browser import browser, Driver,cdp
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
from loguru import logger

#Models

#Modules
from Modules.Extractor import Extractor

@browser(cache=False, reuse_driver=True,headless=False,wait_for_complete_page_load=True)
def zoomit_scraper(driver:Driver, data=None) -> int:
    driver.enable_human_mode()
    driver.detect_and_bypass_cloudflare()
    driver.run_cdp_command(cdp.network.enable())

    logger.info("🌎 Browser successfully initialized")

    #init Extractor
    extractor:Extractor = Extractor()
    extractor.listen_navigation_page(driver)
    logger.info("⚓ Listener hooks successfully inserted")

    driver.get("https://www.zoomit.ir/archive?groupings=32319&sort=Newest&publishDate=All&readingTime=All&pageNumber=2", bypass_cloudflare=True)
    driver.long_random_sleep()

    extractor.extract_navigation_articles_datetime(driver)

    return 0

if __name__ == '__main__':
    zoomit_scraper()