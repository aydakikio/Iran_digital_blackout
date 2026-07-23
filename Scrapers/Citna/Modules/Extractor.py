from bs4 import BeautifulSoup,Tag
from collections import deque
import jdatetime
from datetime import datetime
from zoneinfo import ZoneInfo
import re

#Models
from Scrapers.Citna.Models.comment_data import Comment
from Scrapers.Citna.Models.news_data import News

#Modules
from Scrapers.Citna.Modules.Database_manager import Database_Manager

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
            published_datetime=article.find('div',class_='field--name-node-post-date').get_text(strip=True)

            #check if it is int the range or not

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

        # Save into database
        Database_Manager.save_news(news)

        #Extract the comments
        Extractor.extract_comments(html_content, news.news_uuid)

    
    @staticmethod
    def extract_comments(html_content:BeautifulSoup,news_uuid:str):
        comment_wrapper:Tag = html_content.find('section', class_=["field--name-comment", "field--type-comment","comment-wrapper"])

        replies=deque()
        for I,child_tag in enumerate(comment_wrapper.children):
            if not isinstance(child_tag, Tag):
                continue

            #check if it is comment or a reply
            if child_tag.name == 'div':
                if 'layout--onecol' in (child_tag.get('class') or []): #It is a comment

                    #create data object
                    comment:Comment = Comment()

                    #Getting Author
                    comment.author=child_tag.find('div', class_=['field--name-comment-title']).get_text(strip=True)

                    #Getting Datetime
                    comment.published_time=Extractor.parse_jalali_datetime(child_tag.find('div',class_=['field--name-comment-post-date']).get_text(strip=True))

                    #Getting comment body
                    comment.body=child_tag.find('div',class_=['field--name-field-body']).get_text()

                    like_wrapper= child_tag.find('div', class_=['flag-likecomment'])

                    #Getting comment id
                    comment.comment_id= re.search(r'/likecomment/(\d+)/', like_wrapper.find('a')['href']).group(1)

                    #Getting like counts
                    comment.likes=int(like_wrapper.find('span').get_text(strip=True)[1:-1])

                    #Save into the database
                    Database_Manager.save_comment(comment)

                else: #It is a reply

                    print()

    @staticmethod
    def parse_jalali_datetime(datetime_string: str) -> datetime:
        cleaned = re.sub(r'\s+-\s+', ' ', datetime_string.strip())

        iran_timezone = ZoneInfo("Asia/Tehran")

        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                jalali_datetime = jdatetime.datetime.strptime(cleaned, fmt).replace(tzinfo=iran_timezone)
                return jalali_datetime.togregorian().astimezone(ZoneInfo("UTC"))
            except ValueError:
                continue

        raise ValueError(f"Unrecognized datetime format: '{datetime_string}'")
