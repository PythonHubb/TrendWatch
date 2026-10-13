
from .google_trends import get_trend_data
from trendwatch.validation import validate_topic, validate_score
from datetime import datetime
from .models import Trend




def analyze_trend(topic):
    
    topic = validate_topic(topic)

    data = get_trend_data(topic)

    if data is None or data.empty:
        return {
            "topic": topic,
            "score": 0,
            "status": "No Data",
            "direction": "Unknown"
        }

    scores = data[topic].dropna()

    if scores.empty:
        return {
            "topic": topic,
            "score": 0,
            "status": "No Data",
            "direction": "Unknown"
        }
    
    score = validate_score(round(scores.mean(), 1))

    if score >= 80:
        status = "High Interest"
    elif score >= 60:
        status = "Medium Interest"
    else:
        status = "Low Interest"

    if len(scores) < 2:
        direction = "Not Enough Data"
    elif scores.iloc[-1] > scores.iloc[0]:
        direction = "Rising"
    elif scores.iloc[-1] < scores.iloc[0]:
        direction = "Falling"
    
    else:
        direction = "Stable"

    trend = Trend(
        topic=topic,
        source="Google Trends",
        score=score,
        timestamp=datetime.now(),
        status=status
    )

    
    return {
        "topic": trend.topic,
        "score": trend.score,
        "status": trend.status,
        "direction": direction
    }

