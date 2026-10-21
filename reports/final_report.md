# Premier League 2024–25: Football Data Analysis

## 1. Introduction

This project analyses the 2024–25 English Premier League season using Python and data analysis libraries. The main objectives are to calculate league standings, examine team performance, compare home and away results, and investigate whether the data shows evidence of a home advantage.

The project uses pandas for data manipulation, NumPy for numerical operations, and Matplotlib for visualizations.

## 2. Dataset

The dataset is stored in `data/raw/epl_2024_25.csv` and contains match-level results for the 2024–25 Premier League season.

The dataset contains 380 matches involving 20 teams.

Relevant columns include:

- `Date`: Match date.
- `HomeTeam`: Home team.
- `AwayTeam`: Away team.
- `FTHG`: Full-time home goals.
- `FTAG`: Full-time away goals.
- `FTR`: Full-time result (`H` = home win, `A` = away win, `D` = draw).
- `HS` and `AS`: Shots by the home and away teams.
- `HST` and `AST`: Shots on target by the home and away teams.

## 3. Methodology

### 3.1 Data preparation

The analysis selects the columns required for the investigation, converts numerical fields to appropriate types, and checks for missing or invalid essential match data.

### 3.2 League table calculation

For each team, the following metrics are calculated:

- Matches played (MP)
- Wins (W)
- Draws (D)
- Losses (L)
- Goals for (GF)
- Goals against (GA)
- Goal difference (GD = GF − GA)
- Points (Points = 3 × W + D)

Teams are sorted by points, goal difference, and goals scored.

### 3.3 Home and away performance

The analysis calculates home wins, away wins, home goals, and away goals for each team. Home and away win percentages are calculated using 19 matches per team in each setting.

League-wide home wins, away wins, and draws are counted directly from the match-level results so that each match is counted exactly once.

## 4. Visualizations

The project uses the following visualizations to investigate team and league performance.

### 4.1 League points by team

A bar chart compares the points earned by each team and helps identify the strongest teams based on the final standings.

### 4.2 Goals for versus goals against

A labelled scatter plot compares goals scored with goals conceded. It helps identify teams that combine strong attacking output with effective defending.

### 4.3 Home wins versus away wins

A grouped bar chart compares the number of home and away wins for each team.

### 4.4 Home goals versus away goals

A grouped bar chart compares each team's goals scored at home and away.

### 4.5 Match result distribution

A pie chart displays the proportions of matches ending in home wins, away wins, and draws.

### 4.6 Points versus goal difference

A scatter plot examines the relationship between a team's goal difference and its total league points.

### 4.7 Home win percentage versus away win percentage

A grouped bar chart compares each team's home and away win rates, accounting for the 19 matches played in each setting.

## 5. Key findings

Complete this section after validating the calculations and reviewing the charts.

- **League leaders:** [Insert the team finishing first and its points total.]
- **Strongest attack:** [Insert the team with the most goals scored and its total.]
- **Strongest defence:** [Insert the team with the fewest goals conceded and its total.]
- **Home performance:** [Insert the verified home-win count and percentage.]
- **Away performance:** [Insert the verified away-win count and percentage.]
- **Draws:** [Insert the verified draw count and percentage.]
- **Home versus away scoring:** [Summarize the comparison using the calculated totals.]
- **Goal difference and points:** [Describe the relationship observed in the scatter plot.]

All numerical findings should be based on the validated dataset and calculated results.

## 6. Limitations

This analysis covers a single Premier League season. The results may not generalize to other seasons or leagues.

The dataset contains match outcomes and selected match statistics but does not establish why a team performed well or poorly. Factors such as injuries, tactics, player quality, travel, scheduling, and managerial changes are not fully accounted for.

Differences between home and away performance show associations, not proof that playing at home caused better results.

The conclusions also depend on the accuracy and completeness of the original dataset and the correctness of the calculations.

## 7. Conclusion

This project demonstrates a complete introductory football data analysis workflow, from loading and preparing match data to calculating league standings, comparing home and away performance, and producing visualizations.

The resulting tables and charts provide a structured way to explore team performance and patterns in match outcomes. The project also establishes reusable Python modules for data preparation, statistical calculations, and visualization, making future analyses easier to maintain and extend.
