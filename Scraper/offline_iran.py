#This scrapes the https://offlineiran.com/ website
#This website contains the people experiences from internet black out in Iran

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from bs4 import BeautifulSoup
from collections import deque

#Modules
from Scraper.Modules.Extractors.offline_iran_Extractor import offline_iran_extractor
from Scraper.Modules.Interactors.offline_iran_Interactor import offline_iran_interactor
from Scraper.Modules.Database_Managers.Unauthenticated.offline_iran_database_manager import database_manger
from Scraper.Models.Experience_offline_iran import Experience_Data

#global variables
scrolls:int = 0
is_reached_end =False
pending_experiences: deque[Experience_Data] = deque()


#CREATE A TASK SCHEDULE FOR FINISHING THE 
@browser(cache=False, reuse_driver=True)
def offline_iran_scraper(driver:Driver, data=None) -> int:
    global scrolls
    global pending_experiences

    driver.enable_human_mode()
    bypass_if_detected(driver)

    driver.get("https://offlineiran.com/", bypass_cloudflare=True, timeout=120)
    driver.long_random_sleep()

    offline_iran_interactor.expand_all_texts(driver)

    driver.long_random_sleep()

    #webpage_content:BeautifulSoup = soupify(driver) ->works

    #offline_iran_extractor.extract_experiences(webpage_content , scrolls )
    #offline_iran_interactor.scroll_for_new_comments(driver) -> works

    scrolls+=1

    driver.prompt("wwwaaaaaiiiitttt")
    return 0

if __name__ == '__main__':
    offline_iran_scraper()
