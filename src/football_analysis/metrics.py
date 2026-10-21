
import pandas as pd


def calculate_league_table(matches: pd.DataFrame) -> pd.DataFrame:
    """Calculate league standings from match results."""
    teams = sorted(
        set(matches["HomeTeam"]) | set(matches["AwayTeam"])
    )

    stats = {}

    for team in teams:
        home = matches[matches["HomeTeam"] == team]
        away = matches[matches["AwayTeam"] == team]

        home_wins = int((home["FTR"] == "H").sum())
        away_wins = int((away["FTR"] == "A").sum())

        home_draws = int((home["FTR"] == "D").sum())
        away_draws = int((away["FTR"] == "D").sum())

        home_losses = int((home["FTR"] == "A").sum())
        away_losses = int((away["FTR"] == "H").sum())

        wins = home_wins + away_wins
        draws = home_draws + away_draws
        losses = home_losses + away_losses

        gf = int(home["FTHG"].sum() + away["FTAG"].sum())
        ga = int(home["FTAG"].sum() + away["FTHG"].sum())

        stats[team] = {
            "MP": len(home) + len(away),
            "W": wins,
            "D": draws,
            "L": losses,
            "GF": gf,
            "GA": ga,
            "GD": gf - ga,
            "Points": 3 * wins + draws,
            "HomeWins": home_wins,
            "AwayWins": away_wins,
            "HomeGoals": int(home["FTHG"].sum()),
            "AwayGoals": int(away["FTAG"].sum()),
        }

    table = pd.DataFrame.from_dict(stats, orient="index")
    table.index.name = "Team"

    return table.sort_values(
        by=["Points", "GD", "GF"],
        ascending=[False, False, False]
    )


def calculate_result_summary(matches: pd.DataFrame) -> dict:
    """Summarize league-wide match results."""
    total = len(matches)

    if total == 0:
        raise ValueError("Cannot summarize an empty match dataset.")

    home_wins = int((matches["FTR"] == "H").sum())
    draws = int((matches["FTR"] == "D").sum())
    away_wins = int((matches["FTR"] == "A").sum())

    return {
        "TotalMatches": total,
        "Home_Wins": home_wins,
        "Away_Wins": away_wins,
        "Draws": draws,
        "HomeWinPct": round(home_wins / total * 100, 2),
        "AwayWinPct": round(away_wins / total * 100, 2),
        "DrawPct": round(draws / total * 100, 2),
    }
