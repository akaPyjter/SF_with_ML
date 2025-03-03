from datetime import datetime
from enum import Enum

class TimeFrame(Enum):
    ONE_MINUTE = 60
    FIVE_MINUTES = 300
    THIRTY_MINUTES = 1800
    ONE_HOUR = {"api_interval": "1h", "seconds":3600}
    FOUR_HOURS = 14400
    ONE_DAY = 86400

class Symbols(Enum):
    BTCUSDT = "BTCUSDT"

def count_time_from_2010(interval: TimeFrame):
    start_date = datetime(2010, 1, 1)
    now = datetime.now()
    return (now - start_date).total_seconds() / interval






