# 🚀 TrendWatch

**📈 A command-line tool that tells content and marketing teams which topic people are searching for right now.**

Before a team writes an article, plans a campaign or picks a video topic, it needs to know: *Is interest in this topic high? Is it growing or fading? Which of two topics is more popular?* Checking Google Trends by hand for every idea is slow and gives no consistent answer. TrendWatch answers these questions from the terminal in seconds, using live Google Trends data, and turns the raw numbers into a clear verdict. 🎯

```text
$ python -m trendwatch.cli analyze "AI"

--- TrendWatch Analysis ---
Topic: AI
Score: 72.4
Status: Medium Interest
Direction: Rising
```

*(💡 Numbers are an example; live values change daily.)*

## 📚 Contents

- [✨ Features](#-features)
- [⚙️ How it works](#️-how-it-works)
- [📦 Installation](#-installation)
- [💻 Usage](#-usage)
- [📂 Project structure](#-project-structure)
- [🏗️ Design](#️-design)
- [🛡️ Error handling](#️-error-handling)
- [🧪 Tests](#-tests)
- [⚠️ Limitations](#️-limitations)
- [👥 Team](#-team)

## ✨ Features

| Command | Question it answers | Output |
| --- | --- | --- |
| 🔍 `analyze` | How popular is this topic, and where is it heading? | Average interest score, interest level (Low / Medium / High), direction (Rising / Falling / Stable) |
| ⚖️ `compare` | Which of two topics do people search for more? | Both average scores and the winner, or "Tie" |
| 📊 `plot` | How did the two topics develop over time? | A line chart of both topics over the last 3 months |

## ⚙️ How it works

1. **📡 Data:** TrendWatch requests the last 3 months of search interest (`timeframe="today 3-m"`) from Google Trends through the `pytrends` library. Google Trends reports interest as a **relative value from 0 to 100**: 100 is the topic's peak popularity in the period, not an absolute number of searches.
2. **📊 Score:** the average of all data points, rounded to one decimal place, and checked to be between 0 and 100.
3. **🚦 Interest level:**

    | Average score | Status |
    | --- | --- |
    | 80 – 100 | 🔥 High Interest |
    | 60 – 79.9 | 📈 Medium Interest |
    | 0 – 59.9 | 🌱 Low Interest |

4. **🧭 Direction:** the last data point is compared with the first one: higher → **Rising** 📈, lower → **Falling** 📉, equal → **Stable** ➡️. With fewer than two data points the result is **Not Enough Data**.
5. **⚖️ Comparison:** both topics are requested **in one Google Trends query**, so their scores are on the same 0–100 scale and can be compared directly. Google's `isPartial` column (marking an incomplete last week) is removed before averaging.

## 📦 Installation

Requires **Python 3.10 or newer** 🐍 and an internet connection 🌐 for live data.

```powershell
git clone https://github.com/PythonHubb/TrendWatch.git
cd TrendWatch

python -m venv .venv
.\.venv\Scripts\Activate.ps1          # Windows PowerShell
# source .venv/bin/activate           # macOS / Linux

python -m pip install -r requirements.txt        # pytrends, pandas, matplotlib
python -m pip install -r requirements-dev.txt    # pytest, ruff (for development)
```

## 💻 Usage

Run every command from the project root (the folder that contains `trendwatch/`). Put topics that contain spaces in quotes.

### 🔍 Analyze one topic

```powershell
python -m trendwatch.cli analyze "AI"
```

### ⚖️ Compare two topics

```powershell
python -m trendwatch.cli compare "AI" "Bitcoin"
```

```text
--- TrendWatch Comparison ---
AI: 72.4
Bitcoin: 41.3
Higher search interest: AI
```

### 📊 Plot two topics

```powershell
python -m trendwatch.cli plot "AI" "Bitcoin"
```

Opens a window with a line chart of both topics (x-axis: date, y-axis: interest 0–100).

### ❓ Help

```powershell
python -m trendwatch.cli --help
```

| Argument | Allowed values | Rule |
| --- | --- | --- |
| `command` | `analyze`, `compare`, `plot` | Any other value is rejected by argparse |
| `topics` | one or more topics | `analyze` needs exactly 1; `compare` and `plot` need exactly 2 |

## 📂 Project structure

```text
TrendWatch/
├── trendwatch/              The application package
│   ├── __init__.py
│   ├── cli.py
│   ├── analyzer.py
│   ├── comparator.py
│   ├── google_trends.py
│   ├── visualizer.py
│   ├── models.py
│   └── validation.py
├── tests/                   Automated tests (pytest)
│   ├── test_analyzer.py
│   ├── test_comparator.py
│   ├── test_models.py
│   └── test_validation.py
├── contributions/           One file per team member
├── requirements.txt         Runtime dependencies
├── requirements-dev.txt     Development dependencies
├── README.md
└── .gitignore
```

### 🗂️ What each file is for

| File | Responsibility |
| --- | --- |
| `trendwatch/__init__.py` | Marks `trendwatch` as a Python package, so it can be run with `python -m trendwatch.cli` and its modules can import each other |
| `trendwatch/cli.py` | Entry point. Defines the command-line arguments with `argparse`, checks the number of topics for each command, calls the matching function and prints the result |
| `trendwatch/google_trends.py` | `get_trend_data(topic)`: the only place that downloads data for a single topic from Google Trends. Handles the rate-limit error (HTTP 429) and empty results by returning `None` |
| `trendwatch/analyzer.py` | `analyze_trend(topic)`: validates the topic, gets the data, computes the average score, the interest level and the direction, and returns them as a dictionary |
| `trendwatch/comparator.py` | `compare_trends(topic1, topic2)`: requests both topics in one query, averages each, and returns the scores and the winner as a dictionary |
| `trendwatch/visualizer.py` | `plot_trends(topic1, topic2)`: requests both topics and draws a labelled line chart with `matplotlib` |
| `trendwatch/models.py` | `Trend` dataclass: one analysed topic (topic, source, score, timestamp, status) |
| `trendwatch/validation.py` | `validate_topic` (non-empty text, trimmed) and `validate_score` (a real number between 0 and 100, booleans rejected) |
| `tests/test_analyzer.py` | Scoring thresholds, every direction, single data point, no data |
| `tests/test_comparator.py` | First wins, second wins, tie, empty data, `isPartial` column ignored |
| `tests/test_models.py` | Creating a `Trend`, its default status, timestamp type, status update |
| `tests/test_validation.py` | Valid, empty, negative, zero, maximum, out-of-range and wrong-type inputs |
| `contributions/` | `NAME_SURNAME_STUDENTID_GITHUBUSER.md` for each member, describing their work |
| `requirements.txt` | Packages needed to run TrendWatch |
| `requirements-dev.txt` | Extra packages for development: `pytest` for tests, `ruff` for code-style checks |
| `.gitignore` | Keeps the virtual environment, editor settings and Python caches out of the repository |

## 🏗️ Design

```text
cli.py ──analyze──▶ analyzer.py ──▶ google_trends.py ──▶ pytrends ──▶ Google Trends
   │                    │
   │                    ├──▶ validation.py   (topic and score checks)
   │                    └──▶ models.py       (Trend dataclass)
   ├──compare──▶ comparator.py ──▶ pytrends
   └──plot─────▶ visualizer.py ──▶ pytrends + matplotlib
```

- **🧩 Separation of concerns:** the CLI only parses arguments and prints. Fetching, analysing, comparing and plotting each live in their own module, so each can be tested on its own.
- **📦 Data model:** `Trend` is a `@dataclass`, which generates `__init__`, `__repr__` and `__eq__` from the fields.
- **📋 Dictionaries as results:** `analyze_trend` and `compare_trends` return dictionaries (`result["status"]`, `result["winner"]`), which keeps the CLI independent of how the values were computed.
- **🐼 pandas:** Google Trends data arrives as a `DataFrame` with one column per topic. TrendWatch uses `dropna()`, `mean()`, `iloc[0]` / `iloc[-1]` and `drop(columns=["isPartial"])`.
- **✅ Validation:** `validate_score` rejects `True` / `False` explicitly, because `bool` is a subclass of `int` in Python.

## 🛡️ Error handling

| Situation | Behaviour |
| --- | --- |
| ❌ Unknown command (e.g. `delete`) | argparse prints the allowed choices and exits |
| ⚠️ Wrong number of topics | Clear message, e.g. *"Compare requires two topics"* |
| 🚦 Google Trends rate limit (HTTP 429) | *"Google Trends rate limit reached (429). Please try again later."* |
| 📭 No data for a topic | `analyze` reports **No Data**; `compare` prints *"No comparison data found."* |
| 🚫 Empty topic in `analyze` | Rejected by `validate_topic` with a `ValueError` |

## 🧪 Tests

```powershell
python -m pytest tests/ -v
```

**✅ 23 tests** (analyzer 6, comparator 5, models 4, validation 8). They run **without internet access**: `unittest.mock.patch` replaces the Google Trends calls with prepared `pandas` DataFrames, so every case — high, medium and low interest, rising, falling and stable trends, ties, empty data — can be tested on demand and gives the same result every time.

## ⚠️ Limitations

- **🌐 Google Trends has no official public API.** `pytrends` uses Google's website endpoints, which may answer with HTTP 429 (too many requests) or change without notice. Waiting a minute usually helps.
- **📊 Scores are relative (0–100)**, not search counts: they show popularity within the chosen period, not how many people searched.
- **📅 The time window** is fixed to the **last 3 months**.
- **🖥️ `plot`** needs a desktop session that can open a chart window.

## 👥 Team

| Name | Student ID | GitHub | Role in the project | Details |
| --- | --- | --- | --- | --- |
| Seyedfarnam Niroomand | 2509015231 | [@Farnam-N](https://github.com/Farnam-N) | 🎤 Presenter; command-line interface and error handling (`cli.py`) | [contribution](contributions/SEYEDFARNAM_NIROOMAND_2509015231_Farnam-N.md) |
| Rosha Vafaee Shahi | 2309116505 | [@roshavafaei](https://github.com/roshavafaei) | 🚀 Project lead; repository, package structure, README and requirements | [contribution](contributions/ROSHA_VAFAEE_SHAHI_2309116505_roshavafaei.md) |
| Mohamed A Khalifa Omar | 2509115214 | [@mohamedelmismary](https://github.com/mohamedelmismary) | 📈 Google Trends data and trend analysis (`google_trends.py`, `analyzer.py`, `models.py`) | [contribution](contributions/MOHAMED_A_KHALIFA_OMAR_2509115214_mohamedelmismary.md) |
| Borna Anlar | 2509115360 | [@borna111184-creator](https://github.com/borna111184-creator) | 📊 Comparison, charts and input validation (`comparator.py`, `visualizer.py`, `validation.py`) | [contribution](contributions/BORNA_ANLAR_2509115360_borna111184-creator.md) |

Each member's full description of their work is in the [`contributions/`](contributions/) folder.

---

**🚀 TrendWatch — Turn search trends into smarter content decisions!**