# 👨‍💻 Contribution — Seyedfarnam Niroomand

| | |
| --- | --- |
| **Student ID** | 2509015231 |
| **GitHub** | [@Farnam-N](https://github.com/Farnam-N) |
| **Role** | Presenter; command-line interface and error handling |
| **Commits** | [https://github.com/PythonHubb/TrendWatch/commits?author=Farnam-N](https://github.com/PythonHubb/TrendWatch/commits?author=Farnam-N) |

## 📌 Summary

I built the command-line interface, the part of TrendWatch the user interacts with, and I presented the project.

## 💻 Work

### `trendwatch/cli.py`
- Defined the interface with `argparse`: a positional `command` limited to `analyze`, `compare` and `plot` through `choices`, and one or more `topics` through `nargs="+"`.
- Checked the number of topics for each command (`analyze` exactly one, `compare` and `plot` exactly two) and reported mistakes with `parser.error()`, which prints the usage line and exits with code 2.
- Connected each command to its module: `analyze_trend`, `compare_trends` and `plot_trends`.
- Printed the results from the dictionaries those functions return, e.g. `result["status"]` and `result["winner"]`.
- Added input checks and error handling so every topic is validated and a network or input problem produces a one-line message instead of a Python traceback.
- Made the CLI runnable as a module (`python -m trendwatch.cli`) with the `if __name__ == "__main__":` guard.

### 🎤 Presentation
- Prepared the slides and the two-minute talk, and explained the code snippets in class.

## 🛠️ Python techniques used
- `argparse`: positional arguments, `choices`, `nargs`, `parser.error()`
- Reading results from dictionaries
- Relative imports inside a package
- `if __name__ == "__main__":`
- Exception handling with `try` / `except`