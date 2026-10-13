
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError


def plot_trends(topic1, topic2):
    pytrends = TrendReq(hl="en-US", tz=0)
    
    try:
        pytrends.build_payload(
            kw_list=[topic1, topic2],
            timeframe="today 3-m"
        )

        data = pytrends.interest_over_time()

    except TooManyRequestsError:
        print("Google Trends rate limit reached (429). Please try again later.")
        return
    

    if data.empty:
        print("No trend data found.")
        return

    plt.figure(figsize=(10, 5))

    plt.plot(
        data.index,
        data[topic1],
        label=topic1
    )

    plt.plot(
        data.index,
        data[topic2],
        label=topic2
    )

    plt.title("TrendWatch - Trend Comparison")
    plt.xlabel("Date")
    plt.ylabel("Google Trends Interest (0-100)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
