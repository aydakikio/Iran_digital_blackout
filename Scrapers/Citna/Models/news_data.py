from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class News:
    url: str = "None"
    title: str = "None"
    description:str = "None"
    body: str = "None"
    news_code: str = "None"
    reporter: str = "None"
    likes:int = 0

    tags: list[str] = field(default_factory=list)
    published_time: datetime = field(default_factory=datetime.now)
    news_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))