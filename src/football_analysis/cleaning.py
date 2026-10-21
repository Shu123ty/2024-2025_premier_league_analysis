
import pandas as pd


REQUIRED_COLUMNS = [
    "Date", "HomeTeam", "AwayTeam",
    "FTHG", "FTAG", "FTR",
    "HS", "AS", "HST", "AST"
]


def prepare_matches(df: pd.DataFrame) -> pd.DataFrame:
    """Select and validate the columns needed for match analysis."""
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    matches = df[REQUIRED_COLUMNS].copy()

    matches["Date"] = pd.to_datetime(
        matches["Date"], dayfirst=True, errors="coerce"
    )

    numeric_columns = ["FTHG", "FTAG", "HS", "AS", "HST", "AST"]

    for column in numeric_columns:
        matches[column] = pd.to_numeric(
            matches[column], errors="coerce"
        )

    matches = matches.dropna(
        subset=["HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]
    )

    matches = matches[
        matches["FTR"].isin(["H", "D", "A"])
    ].copy()

    return matches.reset_index(drop=True)
