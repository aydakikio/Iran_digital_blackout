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
    def scroll_for_new_comments():
        print()