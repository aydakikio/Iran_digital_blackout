from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Comment:
    body:str = "None"
    author:str = "None"
    likes:int = 0
    comment_id:str = "None"
    news_uuid:str = "None"
    replied_comment:str = "None"

    published_time: datetime = field(default_factory=datetime.now)
    comment_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
