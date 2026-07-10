from bs4 import BeautifulSoup,Tag
from collections import deque
import jdatetime
from datetime import datetime , date
from zoneinfo import ZoneInfo

class Extractor :
    @staticmethod
    def extract_news_link(html_content:BeautifulSoup, pending_news:deque):
        articles_wrapper:Tag = html_content.find("div",class_='item-list')

        articles:Tag=articles_wrapper.find('ul')

        for article in articles.children:

            if not isinstance(article, Tag):
                continue

            published_datetime=article.find('div',class_='field--name-node-post-date').get_text(strip=True).replace(' - ','').strip()
            print(f'raw::: {published_datetime}')
            print(f'transformed:::: {Extractor.parse_jalali_datetime(published_datetime)}')


    @staticmethod
    def extract_news(html_content:BeautifulSoup):
        print()


    @staticmethod
    def extract_comments():
        print()

    @staticmethod
    def parse_jalali_datetime(datetime_string: str) -> datetime:
        iran_timezone = ZoneInfo("Asia/Tehran")
        jalali_datetime = jdatetime.datetime.strptime(datetime_string.strip(), "%Y-%m-%d %H:%M").replace(tzinfo=iran_timezone)

        return jalali_datetime.togregorian().astimezone(ZoneInfo("UTC"))

