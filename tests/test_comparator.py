import pandas as pd
from unittest.mock import patch
from pytrends.exceptions import TooManyRequestsError

from trendwatch.comparator import compare_trends


def mock_trends(data):
    """Create a fake Google Trends response."""
    with patch("trendwatch.comparator.TrendReq") as mock_class:
        mock_client = mock_class.return_value
        mock_client.interest_over_time.return_value = data
        yield mock_client


def test_compare_first_topic_wins():
    data = pd.DataFrame({
        "AI": [80, 90, 100],
        "Bitcoin": [40, 50, 60],
    })

    with patch("trendwatch.comparator.TrendReq") as mock_class:
        mock_class.return_value.interest_over_time.return_value = data

        result = compare_trends("AI", "Bitcoin")

    assert result["winner"] == "AI"
    assert result["score1"] == 90.0
    assert result["score2"] == 50.0


def test_compare_second_topic_wins():
    data = pd.DataFrame({
        "AI": [20, 30, 40],
        "Bitcoin": [70, 80, 90],
    })

    with patch("trendwatch.comparator.TrendReq") as mock_class:
        mock_class.return_value.interest_over_time.return_value = data

        result = compare_trends("AI", "Bitcoin")

    assert result["winner"] == "Bitcoin"
    assert result["score1"] == 30.0
    assert result["score2"] == 80.0


def test_compare_equal_scores():
    data = pd.DataFrame({
        "AI": [60, 70, 80],
        "Python": [80, 70, 60],
    })

    with patch("trendwatch.comparator.TrendReq") as mock_class:
        mock_class.return_value.interest_over_time.return_value = data

        result = compare_trends("AI", "Python")

    assert result["winner"] == "Tie"
    assert result["score1"] == 70.0
    assert result["score2"] == 70.0


def test_compare_empty_data():
    data = pd.DataFrame()

    with patch("trendwatch.comparator.TrendReq") as mock_class:
        mock_class.return_value.interest_over_time.return_value = data

        result = compare_trends("AI", "Bitcoin")

    assert result is None


def test_compare_ignores_ispartial():
    data = pd.DataFrame({
        "AI": [70, 80, 90],
        "Bitcoin": [40, 50, 60],
        "isPartial": [False, False, True],
    })

    with patch("trendwatch.comparator.TrendReq") as mock_class:
        mock_class.return_value.interest_over_time.return_value = data

        result = compare_trends("AI", "Bitcoin")

    assert result["score1"] == 80.0
    assert result["score2"] == 50.0
    assert result["winner"] == "AI"