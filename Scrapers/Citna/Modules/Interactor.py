#Libararies
from botasaurus.browser import Driver, Wait

class Interactor:

    @staticmethod
    def click_on_next_news_page(driver:Driver):
        next_page_button = driver.select('a[title="برو به صفحه بعدی"]',wait=Wait.VERY_LONG)
        
        if next_page_button:
            next_page_button.click(wait=Wait.VERY_LONG)

    @staticmethod
    def click_on_next_comment_page(driver:Driver)->bool:
        next_page_button=driver.select('a[title="برو به صفحه بعدی"]',wait=Wait.VERY_LONG)

        if next_page_button:
            next_page_button.click(wait=Wait.VERY_LONG)
            return True

        return False
