# 👩‍💻 Contribution — Rosha Vafaee Shahi

| | |
| --- | --- |
| **Student ID** | 2309116505 |
| **GitHub** | [@roshavafaei](https://github.com/roshavafaei) |
| **Role** | Project lead; repository, package structure, README and requirements |
| **Commits** | [https://github.com/PythonHubb/TrendWatch/commits?author=roshavafaei](https://github.com/PythonHubb/TrendWatch/commits?author=roshavafaei) |

## 📌 Summary

I set up the repository and the package structure, brought the modules together into one working project, and wrote the documentation.

## 💻 Work

### 📂 Repository and package structure
- Created the GitHub repository and organised the code as a Python package, `trendwatch/`, with an `__init__.py`, so the modules import each other with relative imports and the program runs with `python -m trendwatch.cli`.
- Separated the code into focused modules: data access (`google_trends.py`), analysis (`analyzer.py`), comparison (`comparator.py`), charts (`visualizer.py`), data model (`models.py`), validation (`validation.py`) and the CLI (`cli.py`).
- Wrote `.gitignore` so the virtual environment, editor settings and Python caches stay out of the repository.

### 📦 Dependencies
- `requirements.txt` for the runtime packages (`pytrends`, `pandas`, `matplotlib`) and `requirements-dev.txt` for development (`pytest`, `ruff`), which includes the first file with `-r`.

### 📝 `README.md`
- Business problem, features, how the score, interest level and direction are calculated, installation, usage of every command, a table of what each file is for, the design, error handling, tests, limitations and the team.

### 🤝 Coordination
- Divided the work between the team members, reviewed the modules, and made sure the test suite passes before each push.

## 🛠️ Python techniques used
- Packages and modules, relative imports, running a package module with `-m`
- Virtual environments and dependency files
- Project documentation in Markdown