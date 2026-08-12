from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Users:
    username:str = None
    user_id:str = None