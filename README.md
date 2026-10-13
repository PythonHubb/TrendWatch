# TrendWatch

TrendWatch is a Python command-line application for analyzing, comparing, and visualizing online search trends using Google Trends data.

## Features

- Analyze Google Trends search interest for a topic
- Calculate average interest scores
- Classify interest as Low, Medium, or High
- Identify rising, falling, or stable trends
- Compare search interest between two topics
- Visualize trends using line charts
- Run commands through a command-line interface (CLI)
- Run automated tests with pytest

## Project Structure

```text
trendwatch-cli/
├── trendwatch/
│   ├── __init__.py
│   ├── cli.py
│   ├── analyzer.py
│   ├── comparator.py
│   ├── google_trends.py
│   ├── visualizer.py
│   ├── models.py
│   └── validation.py
├── tests/
│   ├── test_analyzer.py
│   ├── test_comparator.py
│   ├── test_models.py
│   └── test_validation.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
└── .gitignore
```

## Installation

Clone or download the project and open a terminal in the `trendwatch-cli` directory.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install development dependencies for testing:

```powershell
python -m pip install -r requirements-dev.txt
```

## Usage

Run the following commands from the project root directory.

### Analyze a Topic

```powershell
python -m trendwatch.cli analyze "AI"
```

Displays the topic, average interest score, interest classification, and trend direction.

### Compare Two Topics

```powershell
python -m trendwatch.cli compare "AI" "Bitcoin"
```

Compares average Google Trends interest scores and identifies the topic with higher interest, or a tie.

### Visualize Trends

```powershell
python -m trendwatch.cli plot "AI" "Bitcoin"
```

Displays a line chart comparing search interest over time.

## Running Tests

The project uses pytest for automated testing.

Run all tests:

```powershell
python -m pytest tests/ -v
```

Run a specific test module:

```powershell
python -m pytest tests/test_comparator.py -v
```

The latest verified test run completed successfully with **23 passed tests**.

The automated tests use mocked data for the analyzer and comparator, so they do not require live Google Trends requests.

## Data Source

TrendWatch uses Google Trends data through the `pytrends` Python library.

Google Trends interest scores are relative values on a scale from 0 to 100. They do not represent absolute search volumes.

## Technologies

- Python
- argparse
- pandas
- pytrends
- matplotlib
- pytest
- unittest.mock

## Planned Features

- SQLite database integration
- YouTube monitoring
- Reddit integration
- Hacker News integration
- MongoDB support
- Data export functionality
- Interactive CLI menu

## Development Status

TrendWatch is under active development.

The core analysis and comparison functionality has automated test coverage. Live Google Trends requests may occasionally fail due to rate limits (HTTP 429), network problems, or temporary service restrictions.

Automated tests passing does not guarantee that live Google Trends requests will always succeed.