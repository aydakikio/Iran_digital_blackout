#Modules
from Scrapers.Offline_Iran.Models.Experience_offline_iran import Experience_Data
from Scrapers.Offline_Iran.Models.schema_template import ExperienceOfflineIran

#Libararies
from contextlib import contextmanager
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , Session
from typing import Iterator
import os

load_dotenv()

class connection_pool_manager:
    _engine = None
    _SessionLocal = None

    @classmethod
    def _init(cls):
        if cls._engine is not None:
            return

        database_url = os.getenv("OFFLINE_IRAN_DB_URL")

        cls._engine = create_engine(
            database_url,
            pool_size=1,
            max_overflow=0,
            pool_recycle=3600,
            pool_use_lifo=True,
            echo=False
        )
        cls._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._engine)

    @classmethod
    @contextmanager
    def get_session(cls) -> Iterator[Session]:
        if cls._SessionLocal is None:
            cls._init()
        session = cls._SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

class database_manger:
    @staticmethod
    def insert_experience(data:Experience_Data):

        try:
            with connection_pool_manager.get_session() as session:
                new_record = ExperienceOfflineIran(
                    sender_name=data.sender_name,
                    experience_text=data.experience_text,
                    published_date=data.published_date
                )
                session.add(new_record)
        except Exception as e:
            raise RuntimeError(f"Error at insertion {e}")
