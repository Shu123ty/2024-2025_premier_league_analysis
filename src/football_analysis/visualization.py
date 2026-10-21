
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_figure(filename: str, output_dir: str = "outputs/figures"):
    """Save the current Matplotlib figure and close it."""
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    plt.tight_layout()
    plt.savefig(path / filename, dpi=300, bbox_inches="tight")
    plt.close()


def plot_league_points(table: pd.DataFrame):
    """Plot points earned by each team."""
    ax = table["Points"].plot(kind="bar", figsize=(14, 7))

    ax.set_title("Premier League 2024–25: Points by Team")
    ax.set_xlabel("Team")
    ax.set_ylabel("Points")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", alpha=0.3)

    save_figure("league_points.png")


def plot_goals_scatter(table: pd.DataFrame):
    """Plot goals scored against goals conceded."""
    plt.figure(figsize=(12, 8))
    plt.scatter(table["GF"], table["GA"])

    for team, row in table.iterrows():
        plt.annotate(
            team,
            (row["GF"], row["GA"]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
        )

    plt.xlabel("Goals For")
    plt.ylabel("Goals Against")
    plt.title("Goals For vs Goals Against — Premier League 2024–25")
    plt.grid(alpha=0.3)

    save_figure("goals_for_vs_goals_against.png")


def plot_home_away_win_percentage(table: pd.DataFrame):
    """Compare each team's home and away win percentages."""
    x = np.arange(len(table))
    width = 0.4

    plt.figure(figsize=(16, 8))
    plt.bar(
        x - width / 2,
        table["HomeWins"] / 19 * 100,
        width,
        label="Home Win %",
    )
    plt.bar(
        x + width / 2,
        table["AwayWins"] / 19 * 100,
        width,
        label="Away Win %",
    )

    plt.xlabel("Team")
    plt.ylabel("Win Percentage (%)")
    plt.title("Home vs Away Win Percentage — Premier League 2024–25")
    plt.xticks(x, table.index, rotation=45, ha="right")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    save_figure("home_vs_away_win_percentage.png")
