
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError


def compare_trends(topic1, topic2):
    pytrends = TrendReq(hl="en-US", tz=0)

    
    try:
        pytrends.build_payload(
            kw_list=[topic1, topic2],
            timeframe="today 3-m"
        )

        data = pytrends.interest_over_time()

    except TooManyRequestsError:
        print("Google Trends rate limit reached (429). Please try again later.")
        return None


    if data.empty:
        return None

    scores = data.drop(columns=["isPartial"], errors="ignore")

    avg1 = round(scores[topic1].mean(), 1)
    avg2 = round(scores[topic2].mean(), 1)

    if avg1 > avg2:
        winner = topic1
    elif avg2 > avg1:
        winner = topic2
    else:
        winner = "Tie"

    return {
        "topic1": topic1,
        "topic2": topic2,
        "score1": avg1,
        "score2": avg2,
        "winner": winner
    }
