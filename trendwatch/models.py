
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trend:
    topic: str
    source: str
    score: float
    timestamp: datetime
    status: str = "Unknown"
