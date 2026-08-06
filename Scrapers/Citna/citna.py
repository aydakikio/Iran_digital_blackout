#This scrapes the https://www.citna.ir website
#This website contains news about Internet
#Internet Category
#https://www.citna.ir/taxonomy/term/56877?q=taxonomy/term/56877&page=0

#modules
from Modules.Database_manager import Database_Manager
from Modules.Interactor import Interactor
from Modules.Extractor import Extractor

#Models
from Models.news_data import News

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from dotenv import load_dotenv
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
from collections import deque
from datetime import datetime,timezone
from loguru import logger
import os

pending_news:deque[News] = deque()

# 88 day shutdown -> start-> Feb 28 2026 | end -> May 22 2026
# 23 day shutdown -> start -> Jan 8 2026 | end -> Feb 2 2026

@browser(cache=False, reuse_driver=True,headless=True,wait_for_complete_page_load=True)
def citna_scraper(driver:Driver, data=None) -> int:
    global pending_news

    #Create the base node
    database_manager:Database_Manager = Database_Manager(
        uri=os.getenv('DB_URI'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )


    Database_Manager.create_category_node(database_manager,"Internet")
    #Take Screenshots from neo4j

    driver.enable_human_mode()
    bypass_if_detected(driver)

    driver.get(f'https://www.citna.ir/taxonomy/term/58250?page=0', bypass_cloudflare=True)
    driver.long_random_sleep()

    pagination_tab=driver._browser.tabs[0]
    while True:
        webpage_content: BeautifulSoup = soupify(driver)
        Extractor.extract_news_link(webpage_content,pending_news)

        while pending_news:
            news:News = pending_news.popleft()

            #Check to see if it is finished
            if news.published_time < datetime(2026, 2, 28, tzinfo=timezone.utc):
                logger.info("The session is finished successfully")

                database_manager.close()
                return 0

            driver.open_link_in_new_tab(news.url,bypass_cloudflare=True)
            driver.long_random_sleep()

            news_webpage_content: BeautifulSoup = soupify(driver)
            Extractor.extract_news(news_webpage_content,news,database_manager)

            is_comments_not_finished:bool = True

            while is_comments_not_finished is True:
                comments_content: BeautifulSoup = soupify(driver)
                driver.long_random_sleep()

                Extractor.extract_comments(comments_content,news.news_uuid,database_manager)

                is_comments_not_finished=Interactor.click_on_next_comment_page(driver)
            
            driver._tab.close()

            logger.info("Sleeping for 30 seconds 💤")
            driver.sleep(30)#half a minute

        driver.switch_to_tab(pagination_tab)

        logger.info("Sleeping for 30 seconds 💤")
        driver.sleep(30)  # half a minute

        Interactor.click_on_next_news_page(driver)


if __name__ == '__main__':
    load_dotenv()
    citna_scraper()