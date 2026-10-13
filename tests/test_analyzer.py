from trendwatch.analyzer import analyze_trend
from unittest.mock import patch
import pandas as pd


def test_analyze_trend_no_data():
    with patch("trendwatch.analyzer.get_trend_data", return_value=None):
        result = analyze_trend("AI")

    assert result == {"topic": "AI", "score": 0, "status": "No Data", "direction": "Unknown"}


def test_analyze_trend_low_interest():
    data = pd.DataFrame({"AI": [10, 20, 30]})

    with patch("trendwatch.analyzer.get_trend_data", return_value=data):
        result = analyze_trend("AI")

    assert result["score"] == 20.0
    assert result["status"] == "Low Interest"
    assert result["direction"] == "Rising"


def test_analyze_trend_medium_interest():
    data = pd.DataFrame({"AI": [80, 70, 60]})

    with patch("trendwatch.analyzer.get_trend_data", return_value=data):
        result = analyze_trend("AI")

    assert result["score"] == 70.0
    assert result["status"] == "Medium Interest"
    assert result["direction"] == "Falling"


def test_analyze_trend_high_interest():
    data = pd.DataFrame({"AI": [90, 85, 95]})

    with patch("trendwatch.analyzer.get_trend_data", return_value=data):
        result = analyze_trend("AI")

    assert result["score"] == 90.0
    assert result["status"] == "High Interest"
    assert result["direction"] == "Rising"


def test_analyze_trend_stable():
    data = pd.DataFrame({"AI": [50, 50, 50]})

    with patch("trendwatch.analyzer.get_trend_data", return_value=data):
        result = analyze_trend("AI")

    assert result["score"] == 50.0
    assert result["status"] == "Low Interest"
    assert result["direction"] == "Stable"


def test_analyze_trend_single_value():
    data = pd.DataFrame({"AI": [50]})

    with patch("trendwatch.analyzer.get_trend_data", return_value=data):
        result = analyze_trend("AI")

    assert result["score"] == 50.0
    assert result["status"] == "Low Interest"
    assert result["direction"] == "Not Enough Data"