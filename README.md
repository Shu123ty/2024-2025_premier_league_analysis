# Premier League 2024–25: Football Data Analysis

A Python-based exploratory data analysis project investigating team performance, league standings, goals, match outcomes, and home advantage in the 2024–25 English Premier League season.

## Overview

This project uses match-level football data to calculate league standings, compare team performance, and explore patterns in home and away results.

### Objectives

- Calculate the final league table from match results.
- Analyse goals scored, goals conceded, and goal difference.
- Compare home and away wins and goals for each team.
- Examine the distribution of home wins, away wins, and draws.
- Visualize the relationship between league points and goal difference.
- Investigate whether home teams performed better than away teams.

## Technologies

- **Python** — primary programming language
- **pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **Matplotlib** — data visualization
- **JupyterLab** — interactive analysis and experimentation

## Project Structure

```text
football-analysis/
├── data/
│   └── raw/
│       └── epl_2024_25.csv
├── notebooks/
│   └── 01_premier_league_analysis.ipynb
├── outputs/
│   ├── figures/
│   └── tables/
├── reports/
│   └── final_report.md
├── src/
│   └── football_analysis/
│       ├── __init__.py
│       ├── cleaning.py
│       ├── metrics.py
│       └── visualization.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Dataset

The project analyses the 2024–25 Premier League season, consisting of 380 matches and 20 teams.

Important columns include:

| Column | Description |
|---|---|
| `HomeTeam` | Home team |
| `AwayTeam` | Away team |
| `FTHG` | Full-time home goals |
| `FTAG` | Full-time away goals |
| `FTR` | Full-time result |
| `HS`, `AS` | Home and away shots |
| `HST`, `AST` | Home and away shots on target |

The original dataset is stored in `data/raw/epl_2024_25.csv`.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd football-analysis
```

Create and activate a virtual environment.

**Linux/macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Analysis

Launch JupyterLab from the project root:

```bash
jupyter lab
```

Open `notebooks/01_premier_league_analysis.ipynb` and run the notebook cells in order.

The notebook uses the reusable functions in `src/football_analysis/` for data preparation, calculations, and visualization.

If the package is not installed and Python cannot find it, install the project in editable mode after configuring its `pyproject.toml`:

```bash
python -m pip install -e .
```

## Outputs

Generated results are stored in the `outputs/` directory:

- `outputs/figures/` — exported charts in PNG format.
- `outputs/tables/` — exported league tables in CSV format.

The written analysis and interpretation are available in `reports/final_report.md`.

## Methodology

The analysis includes:

1. Selecting and validating relevant match data.
2. Calculating wins, draws, losses, goals for, goals against, goal difference, and league points.
3. Ranking teams by points, goal difference, and goals scored.
4. Comparing home and away performance.
5. Calculating league-wide match result percentages.
6. Producing visualizations to explore team performance and home advantage.

## Limitations

This project examines one season and does not establish that home advantage causes better results. The findings are descriptive and may not generalize to other seasons or competitions.

## Future Improvements

- Analyse multiple Premier League seasons.
- Investigate relationships between shots, shots on target, and goals.
- Add statistical tests for home advantage.
- Compare teams across seasons.
- Build an interactive dashboard for exploring team statistics.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
