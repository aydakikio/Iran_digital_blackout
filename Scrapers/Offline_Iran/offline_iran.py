#This scrapes the https://offlineiran.com/ website
#This website contains the people experiences from internet black out in Iran

#Libararies
from botasaurus.browser import browser, Driver
from botasaurus_driver.solve_cloudflare_captcha import bypass_if_detected
from collections import deque

#Modules
from Scrapers.Offline_Iran.Modules.Interactor import offline_iran_interactor
from Scrapers.Offline_Iran.Models.Experience_offline_iran import Experience_Data
from Scrapers.Offline_Iran.Modules.database_manager import database_manger

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
    #scrolls+=1

    driver.prompt("wwwaaaaaiiiitttt")
    return 0

if __name__ == '__main__':
    #offline_iran_scraper()
    test_data = Experience_Data(
        sender_name="ناشناس، دانش‌آموز",
        experience_text="قطع اینترنت سبب شد من (و خیلی‌های دیگه) به عنوان مخالف جنگ و حمله خارجی نتونیم صدامون رو بلند کنیم.",
        published_date="۱۶ اردیبهشت ۱۴۰۵"
    )

    database_manger.insert_experience(test_data)

