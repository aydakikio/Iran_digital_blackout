#Libarary
from neo4j import GraphDatabase, Driver
from loguru import logger
import uuid

#Models
from Scrapers.Citna.Models.comment_data import Comment
from Scrapers.Citna.Models.news_data import News

class Database_Manager:
    def __init__(self,uri:str, user:str , password:str, max_connection_pool_size: int = 10):
        self.driver:Driver=GraphDatabase.driver(uri=uri,
                                         auth=(user, password),
                                         max_connection_pool_size=max_connection_pool_size)

        self.driver.verify_connectivity()
        logger.info("Connected to Neo4j")

        self.root_uuid: str = str(uuid.uuid4())
        logger.info("Category root node id is created")

    def close(self):
        self.driver.close()
        logger.info("Neo4j connection pool closed")

    def create_category_node(self, category_name: str):
        try:
            with self.driver.session() as session:
                session.run(
                    "MERGE (:Category {name: $name,uuid: $uuid})",
                    name=category_name, uuid=self.root_uuid
                )
        except Exception as error:
            logger.error(f'Error in creating root node: {error}')
            raise ValueError(f'Failed to create root node: {error}') from error

    def save_news(self, news: News):
        try:
            with self.driver.session() as session:
                session.run("""
                    MERGE (root:Category {uuid:$root_uuid})

                    MERGE (news:News {uuid:$uuid})

                    SET news.title = $title,
                        news.url = $url,
                        news.news_code = $news_code,
                        news.reporter = $reporter,
                        news.likes = $likes,
                        news.description = $description,
                        news.body = $body,
                        news.tags = $tags,
                        news.published_time = $published_time

                    MERGE (news)-[:BELONGS_TO]->(root)
                    """,
                            root_uuid=self.root_uuid,
                            uuid=news.news_uuid,
                            title=news.title,
                            url=news.url,
                            news_code=news.news_code,
                            reporter=news.reporter,
                            likes=news.likes,
                            description=news.description,
                            body=news.body,
                            tags=news.tags,
                            published_time=news.published_time.isoformat()
                            )

                logger.info(f'The news {news.news_code} successfully inserted')

        except Exception as error:
            logger.error(f'Error saving news {news.news_code}: {error}')
            raise ValueError(f'Failed to save news {news.news_code}: {error}') from error

    def save_comment(self, comment: Comment):
        try:
            with self.driver.session() as session:

                session.run("""
                    MATCH (news:News {uuid:$news_uuid})

                    MERGE (comment:Comment {uuid:$uuid})

                    SET comment.body = $body,
                        comment.author = $author,
                        comment.likes = $likes,
                        comment.depth = $depth,
                        comment.comment_id = $comment_id,
                        comment.published_time = $published_time

                    MERGE (comment)-[:BELONGS_TO]->(news)

                    WITH comment
                    OPTIONAL MATCH (parent:Comment {uuid:$parent_comment_uuid})

                    FOREACH (_ IN CASE 
                        WHEN parent IS NOT NULL THEN [1]
                        ELSE []
                    END |
                        MERGE (comment)-[:REPLIES_TO]->(parent)
                    )
                    """,
                            uuid=comment.comment_uuid,
                            news_uuid=comment.news_uuid,
                            body=comment.body,
                            author=comment.author,
                            likes=comment.likes,
                            depth=comment.depth,
                            comment_id=comment.comment_id,
                            published_time=comment.published_time.isoformat(),
                            parent_comment_uuid=comment.parent_comment_uuid
                            )

                logger.info(
                    f'Comment {comment.comment_id} successfully inserted'
                )

        except Exception as error:
            logger.error(
                f'Error saving comment {comment.comment_id}: {error}'
            )
            raise ValueError(
                f'Failed to save comment: {error}'
            ) from error