from dataclasses import dataclass
import datetime

@dataclass
class Experience_Data:
    sender_name: str = None
    experience_text: str = None
    published_date: datetime = None