#This scrapes the https://www.citna.ir website
#This website contains news about Internet

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
from collections import deque
import datetime

current_news_page:int = 0

pending_news:deque[str] = deque()
pending_comments:deque[str] = deque()

#url of news page -> https://www.citna.ir/taxonomy/term/56877?q=taxonomy/term/56877&page=0

@browser(cache=False, reuse_driver=True,headless=True)
def citna_scraper(driver:Driver, data=None) -> int:
    global current_news_page

    driver.enable_human_mode()
    bypass_if_detected(driver)

    driver.get(f'https://www.citna.ir/taxonomy/term/56877?q=taxonomy/term/56877&page={current_news_page}')
    print()
    return 0

if __name__ == '__main__':
    print()