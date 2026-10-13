from datetime import datetime
from trendwatch.models import Trend


def test_trend_creation():
    trend = Trend(
        topic="AI",
        source="Google Trends",
        score=85.0,
        timestamp=datetime.now(),
        status="High Interest"
    )

    assert trend.topic == "AI"
    assert trend.source == "Google Trends"
    assert trend.score == 85.0
    assert trend.status == "High Interest"


def test_trend_default_status():
    trend = Trend(
        topic="Bitcoin",
        source="Google Trends",
        score=50.0,
        timestamp=datetime.now()
    )

    assert trend.status == "Unknown"


def test_trend_timestamp():
    trend = Trend(
        topic="AI",
        source="Google Trends",
        score=75.0,
        timestamp=datetime.now()
    )

    assert isinstance(trend.timestamp, datetime)


def test_trend_status_update():
    trend = Trend(
        topic="AI",
        source="Google Trends",
        score=75.0,
        timestamp=datetime.now()
    )

    trend.status = "Medium Interest"

    assert trend.status == "Medium Interest"