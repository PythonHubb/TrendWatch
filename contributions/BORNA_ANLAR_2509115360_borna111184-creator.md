# 👨‍💻 Contribution — Borna Anlar

| | |
| --- | --- |
| **Student ID** | 2509115360 |
| **GitHub** | [@borna111184-creator](https://github.com/borna111184-creator) |
| **Role** | Comparison, charts and input validation |
| **Commits** | [https://github.com/PythonHubb/TrendWatch/commits?author=borna111184-creator](https://github.com/PythonHubb/TrendWatch/commits?author=borna111184-creator) |

## 📌 Summary

I built the comparison of two topics, the trend chart, and the validation of user input.

## 💻 Work

### ⚖️ `trendwatch/comparator.py`
- `compare_trends(topic1, topic2)` requests **both topics in one Google Trends query**, so their scores share the same 0–100 scale and can be compared directly.
- Removes Google's `isPartial` column (`drop(columns=["isPartial"], errors="ignore")`), averages each topic and returns the scores and the winner, or `"Tie"`, as a dictionary.
- Returns `None` for empty data, a rate limit or a network error, and checks both topics before sending the request.

### 📊 `trendwatch/visualizer.py`
- `plot_trends(topic1, topic2)` draws both topics over time with `matplotlib`: title, axis labels, legend and grid.

### ✅ `trendwatch/validation.py`
- `validate_topic` trims whitespace and rejects empty or non-text topics.
- `validate_score` accepts only numbers from 0 to 100 and rejects `True` / `False` explicitly, because `bool` is a subclass of `int` in Python.

## 🧪 Tests
- `tests/test_comparator.py` (5 tests): first topic wins, second wins, tie, empty data, and the `isPartial` column being ignored. `unittest.mock.patch` replaces the `TrendReq` class, so no request reaches Google.
- `tests/test_validation.py` (8 tests): valid, empty, negative, zero, maximum, out-of-range and wrong-type inputs, using `pytest.raises`.

## 🛠️ Python techniques used
- pandas: selecting and dropping columns, `mean()`
- matplotlib: line charts, labels, legend
- Input validation with `isinstance` and range checks
- Raising `ValueError`
- Mocking a class with `unittest.mock.patch`
- `pytest.raises`