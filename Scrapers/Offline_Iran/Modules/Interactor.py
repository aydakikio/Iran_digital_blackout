#must scroll 20*176
#each time it loads 20 comment + and most of comments are in these range of heights 63.5 to 175.5
#most of the heights are 176

#libararies
from botasaurus.browser import Driver

class offline_iran_interactor:

    @staticmethod
    def expand_all_texts(driver:Driver):
        driver.run_js("""
            var btns = document.querySelectorAll('button[aria-label="expand"]');
            Array.from(btns).slice(-20).forEach(b => b.click());
        """)

    @staticmethod
    def scroll_for_new_comments(driver:Driver):
        driver.scroll_into_view('section[class="space-y-10"]')
        driver.scroll(0,3500,smooth_scroll=True)

        driver.sleep(600)#wait for 600 seconds