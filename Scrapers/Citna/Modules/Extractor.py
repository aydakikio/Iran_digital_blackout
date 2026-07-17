from bs4 import BeautifulSoup,Tag
from collections import deque
import jdatetime
from datetime import datetime
from zoneinfo import ZoneInfo

#Models
from Scrapers.Citna.Models.news_data import News

class Extractor :
    @staticmethod
    def extract_news_link(html_content:BeautifulSoup, pending_news:deque):
        articles_wrapper:Tag = html_content.find("div",class_='item-list')

        articles:Tag=articles_wrapper.find('ul')

        for article in articles.children:

            if not isinstance(article, Tag):
                continue

            #extract article link
            partial_link=article.find('a')['href']


            #extract published time
            published_datetime=article.find('div',class_='field--name-node-post-date').get_text(strip=True).replace(' - ','').strip()

            #Add that to queue
            news:News=News()
            news.published_time=Extractor.parse_jalali_datetime(published_datetime)
            news.url=f'https://www.citna.ir{partial_link}'

            pending_news.append(news)


    @staticmethod
    def extract_news(html_content:BeautifulSoup, news:News):

        #Getting news code
        news.news_code= html_content.find('span', class_='nid').get_text(strip=True).replace("کد خبر: ", "")

        #news title
        news.title = html_content.find('div', class_='field--name-node-title').get_text()

        #news description
        news.description = html_content.find('div' , class_='field--name-field-lead').get_text()

        #news body
        news.body = html_content.find('div' , class_='clearfix text-formatted field field--name-body field--type-text-with-summary field--label-visually_hidden').get_text().replace('متن خبر' ,'').replace('انتهای پیام','')

        #news tags links field__items
        news_tag_container = html_content.find('ul' , class_='links field__items')
        for news_tag in news_tag_container.children:
            if not isinstance(news_tag, Tag):
                continue

            news.tags.append(news_tag.get_text(strip=True))


        #news like
        like_wrapper= html_content.find('div', class_=f'js-flag-like-{news.news_code}')
        news.likes = int(like_wrapper.find('span').get_text(strip=True)[1:-1])


    @staticmethod
    def extract_comments():

        print()

    @staticmethod
    def parse_jalali_datetime(datetime_string: str) -> datetime:
        iran_timezone = ZoneInfo("Asia/Tehran")
        jalali_datetime = jdatetime.datetime.strptime(datetime_string.strip(), "%Y-%m-%d %H:%M").replace(tzinfo=iran_timezone)

        return jalali_datetime.togregorian().astimezone(ZoneInfo("UTC"))

