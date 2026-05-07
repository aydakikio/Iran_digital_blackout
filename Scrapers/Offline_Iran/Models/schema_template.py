from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class ExperienceOfflineIran(Base):
    __tablename__ = "experience_offline_iran"

    id = Column(Integer, primary_key=True,autoincrement=True)
    sender_name = Column(String(80), nullable=False)
    experience_text = Column(String(490), nullable=False)
    published_date = Column(DateTime(timezone=True), nullable=False)