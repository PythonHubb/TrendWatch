# 👨‍💻 Contribution — Mohamed A Khalifa Omar

| | |
| --- | --- |
| **Student ID** | 2509115214 |
| **GitHub** | [@mohamedelmismary](https://github.com/mohamedelmismary) |
| **Role** | Google Trends data and trend analysis |
| **Commits** | [https://github.com/PythonHubb/TrendWatch/commits?author=mohamedelmismary](https://github.com/PythonHubb/TrendWatch/commits?author=mohamedelmismary) |

## 📌 Summary

I built the part that downloads data from Google Trends and turns it into a score, an interest level and a trend direction.

## 💻 Work

### 📡 `trendwatch/google_trends.py`
- `get_trend_data(topic)` creates a `pytrends` `TrendReq` client, requests the last three months (`timeframe="today 3-m"`) and returns Google's answer as a pandas `DataFrame`.
- Returns `None` instead of crashing when Google answers with a rate limit (HTTP 429, `TooManyRequestsError`), when the network fails, or when there is no data, so the caller can report "No Data".

### 📈 `trendwatch/analyzer.py`
- `analyze_trend(topic)` validates the topic, gets the data and removes missing values with `dropna()`.
- **Score:** the average with `mean()`, rounded to one decimal and checked with `validate_score`.
- **Interest level:** 80 and above is High, 60 and above is Medium, below 60 is Low.
- **Direction:** compares the last value with the first (`iloc[-1]` and `iloc[0]`): Rising, Falling or Stable; "Not Enough Data" with fewer than two points.
- Returns the result as a dictionary, so the CLI does not depend on how it was calculated.

### 📦 `trendwatch/models.py`
- The `Trend` dataclass (topic, source, score, timestamp, status with the default `"Unknown"`).

## 🧪 Tests
- `tests/test_analyzer.py` (6 tests): no data, low, medium and high interest, a stable trend and a single data point. `unittest.mock.patch` replaces `get_trend_data` with prepared DataFrames, so the tests run without internet.
- `tests/test_models.py` (4 tests): creating a `Trend`, its default status, the timestamp type and updating the status.

## 🛠️ Python techniques used
- `@dataclass` with a default value
- pandas: `DataFrame`, `dropna()`, `mean()`, `iloc`
- Conditional classification with `if` / `elif` / `else`
- Dictionaries as return values
- Exception handling for network and API errors
- Mocking with `unittest.mock.patch`