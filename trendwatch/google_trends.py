from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def get_trend_data(topic):
    pytrends = TrendReq(
        hl="en-US",
        tz=0
    )

    
    try:
        pytrends.build_payload(
            kw_list=[topic],
            timeframe="today 3-m"
        )

        data = pytrends.interest_over_time()

    except TooManyRequestsError:
        print("Google Trends rate limit reached (429). Please try again later.")
        return None



    if data.empty:
        print("No trend data found.")
        return

    return data  