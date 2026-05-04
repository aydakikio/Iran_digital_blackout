#This scrapes the https://offlineiran.com/ website
#This website contains the people experiences from internet black out in Iran

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from bs4 import BeautifulSoup

#Modules
from Scraper.Modules.Extractors.offline_iran_Extractor import offline_iran_extractor
from Scraper.Modules.Interactors.offline_iran_Interactor import offline_iran_interactor

#global variables
scrolls:int = 0
is_reached_end =False

@browser(cache=False, reuse_driver=True,headless=True)
def offline_iran_scraper(driver:Driver, data=None) -> int:
    global scrolls

    driver.enable_human_mode()
    bypass_if_detected(driver)

    driver.get("https://offlineiran.com/", bypass_cloudflare=True, timeout=120)
    driver.long_random_sleep()

    offline_iran_interactor.expand_all_texts(driver)

    driver.long_random_sleep()

    webpage_content:BeautifulSoup = soupify(driver)

    offline_iran_extractor.extract_experiences(webpage_content , scrolls)


    return 0

if __name__ == '__main__':
    offline_iran_scraper()