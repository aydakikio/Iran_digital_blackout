#This scrapes the https://www.citna.ir website
#This website contains news about Internet
#Internet Category
#https://www.citna.ir/taxonomy/term/56877?q=taxonomy/term/56877&page=0

#modules
from Modules.Extractor import Extractor

#Models
from Models.news_data import News

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
from collections import deque
import datetime
import uuid

current_news_page:int = 0

pending_news:deque[News] = deque()
pending_comments:deque[str] = deque()

# 88 day shutdown -> start-> Feb 28 2026 | end -> May 22 2026
# 23 day shutdown -> start -> Jan 8 2026 | end -> Feb 2 2026

@browser(cache=False, reuse_driver=True,headless=True)
def citna_scraper(driver:Driver, data=None) -> int:
    global current_news_page
    global pending_news

    driver.enable_human_mode()
    bypass_if_detected(driver)

    """
    driver.get(f'https://www.citna.ir/taxonomy/term/58250?page={current_news_page}',bypass_cloudflare=True)
    driver.long_random_sleep()

    pagination_webpage_content: BeautifulSoup = soupify(driver)

    Extractor.extract_news_link(pagination_webpage_content,pending_news)
    """
    driver.get(f'https://www.citna.ir/news/335818/%D9%82%D9%88%D9%84-%D9%88%D8%B2%DB%8C%D8%B1-%D8%B9%D9%84%D9%88%D9%85-%D8%AF%D8%B3%D8%AA%D8%B1%D8%B3%DB%8C-%D8%AC%D8%A7%D9%85%D8%B9%D9%87-%D8%B9%D9%84%D9%85%DB%8C-%DA%A9%D8%B4%D9%88%D8%B1-%D8%A7%DB%8C%D9%86%D8%AA%D8%B1%D9%86%D8%AA-%D8%A8%DB%8C%D9%86-%D8%A7%D9%84%D9%85%D9%84%D9%84%DB%8C',bypass_cloudflare=True)
    driver.long_random_sleep()

    news_webpage_content: BeautifulSoup = soupify(driver)

    news:News = News()
    Extractor.extract_news(news_webpage_content,news)


    return 0

if __name__ == '__main__':
    citna_scraper()