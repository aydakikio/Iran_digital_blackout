#libararies
from datetime import datetime,timezone
from bs4 import BeautifulSoup,Tag
from collections import deque
from zoneinfo import ZoneInfo
from loguru import logger
import jdatetime
import re

#Data Classes
from Scrapers.Citna.Models.comment_data import Comment
from Scrapers.Citna.Models.news_data import News

#Modules
from Scrapers.Citna.Modules.Database_manager import Database_Manager

class Extractor :
    @staticmethod
    def extract_news_link(html_content:BeautifulSoup, pending_news:deque) -> None:
        articles_wrapper:Tag = html_content.find("div",class_='item-list')

        articles:Tag=articles_wrapper.find('ul')

        for article in articles.children:

            if not isinstance(article, Tag):
                continue

            #extract article link
            partial_link=article.find('a')['href']


            #extract published time
            published_datetime=Extractor.parse_jalali_datetime(article.find('div',class_='field--name-node-post-date').get_text(strip=True))

            #check if it is int the range or not
            if Extractor.in_range(published_datetime):
                #Add that to queue
                news:News=News()
                news.published_time=published_datetime
                news.url=f'https://www.citna.ir{partial_link}'

                pending_news.append(news)
            else:
                logger.info('News is out of range')

    @staticmethod
    def extract_news(html_content:BeautifulSoup, news:News) -> None:

        #Getting news code
        news.news_code= html_content.find('span', class_='nid').get_text(strip=True).replace("کد خبر: ", "")

        #news title
        news.title = html_content.find('div', class_='field--name-node-title').get_text()

        #news description
        news.description = html_content.find('div' , class_='field--name-field-lead').get_text()

        #news body
        news.body = html_content.find('div' , class_=['field--type-text-with-summary','field--label-visually_hidden']).get_text().replace('متن خبر' ,'').replace('انتهای پیام','')

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
    def extract_comments(html_content: BeautifulSoup, news_uuid: str) -> None:
        comment_wrapper: Tag = html_content.find('section', class_=["comment-wrapper"])

        comment_map: dict[str, str] = {}

        # queue items
        queue: deque[tuple[Tag, str | None, int]] = deque()
        queue.append((comment_wrapper, None, 0))

        while queue:
            wrapper, parent_comment_id, depth = queue.popleft()
            last_comment_id: str | None = parent_comment_id

            for child_tag in wrapper.children:
                if not isinstance(child_tag, Tag):
                    continue
                if child_tag.name != 'div':
                    continue

                classes = child_tag.get('class') or []

                if 'layout--onecol' in classes:
                    comment = Comment()
                    comment.news_uuid = news_uuid
                    comment.depth = depth
                    comment.parent_comment_id = parent_comment_id
                    comment.parent_uuid = comment_map.get(parent_comment_id) if parent_comment_id else None

                    # Getting Author
                    comment.author = child_tag.find('div', class_=['field--name-comment-title']).get_text(strip=True)

                    # Getting Datetime
                    comment.published_time = Extractor.parse_jalali_datetime(
                        child_tag.find('div', class_=['field--name-comment-post-date']).get_text(strip=True)
                    )

                    # Getting comment body
                    comment.body = child_tag.find('div', class_=['field--name-field-body']).get_text()

                    like_wrapper = child_tag.find('div', class_=['flag-likecomment'])

                    # Getting comment id
                    comment.comment_id = re.search(r'/likecomment/(\d+)/', like_wrapper.find('a')['href']).group(1)

                    # Getting like count
                    comment.likes = int(like_wrapper.find('span').get_text(strip=True)[1:-1])

                    # Track in map and update last seen
                    comment_map[comment.comment_id] = comment.comment_uuid
                    last_comment_id = comment.comment_id

                    # Save into the database
                    Database_Manager.save_comment(comment)

                elif 'indented' in classes:
                    queue.append((child_tag, last_comment_id, depth + 1))


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

        logger.error(f"Unrecognized datetime format: '{datetime_string}'")
        raise ValueError(f"Unrecognized datetime format: '{datetime_string}'")

    @staticmethod
    def in_range(dt: datetime) -> bool: #Fix the time and day
        return (
            datetime(2026, 2, 28, tzinfo=timezone.utc) <= dt <= datetime(2026, 5, 26, tzinfo=timezone.utc) #88 days shutdown
            or
            datetime(2026, 1, 8, tzinfo=timezone.utc) <= dt <= datetime(2026, 1, 30, tzinfo=timezone.utc)#23 days shutdown
        )
