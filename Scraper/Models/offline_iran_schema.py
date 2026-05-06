from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from . import Base

class ExperienceOfflineIran(Base):
    __tablename__ = "experience_offline_iran"

    id = Column(Integer, primary_key=True)
    url = Column(String(2048), unique=True, nullable=False)
    title = Column(String(512))
    content = Column(Text)
    source = Column(String(128))
    published_date = Column(DateTime(timezone=True))
    fetched_at = Column(DateTime(timezone=True), server_default=func.now())
    is_processed = Column(Boolean, default=False)