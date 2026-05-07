#This scrapes the https://offlineiran.com/ website
#This website contains the people experiences from internet black out in Iran

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
from collections import deque
import datetime

#Modules
from Scrapers.Offline_Iran.Modules.Extractor import offline_iran_extractor
from Scrapers.Offline_Iran.Modules.Interactor import offline_iran_interactor
from Scrapers.Offline_Iran.Models.Experience_offline_iran import Experience_Data
from Scrapers.Offline_Iran.Modules.database_manager import database_manger

#global variables
scrolls:int = 0

target_date:datetime = datetime.datetime(2026, 2, 27)
pending_experiences: deque[Experience_Data] = deque()

@browser(cache=False, reuse_driver=True)
def offline_iran_scraper(driver:Driver, data=None) -> int:
    global scrolls
    global pending_experiences
    global target_date

    is_finished:bool = False

    driver.enable_human_mode()
    bypass_if_detected(driver)

    driver.get("https://offlineiran.com/", bypass_cloudflare=True, timeout=120)
    driver.long_random_sleep()

    while is_finished is False:
        #Expand all texts
        offline_iran_interactor.expand_all_texts(driver)
        driver.long_random_sleep()

        #Extract data from Webpage
        webpage_content:BeautifulSoup = soupify(driver)
        offline_iran_extractor.extract_experiences(webpage_content , scrolls,pending_experiences )

        #Store all of extracted data
        while pending_experiences:
            experience=pending_experiences.popleft()
            if experience.published_date <= target_date:
                is_finished =True
                break

            database_manger.insert_experience(experience)


        offline_iran_interactor.scroll_for_new_comments(driver)
        scrolls+=1

    return 0

if __name__ == '__main__':
    offline_iran_scraper()

