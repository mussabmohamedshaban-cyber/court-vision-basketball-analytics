# court_vision_analytics.py — Basketball Player Performance & Morale Impact Analyzer
# Built on Linux Mint in Libya | Applies Google Data Analytics & CS50x (Weeks 3-4) algorithmic sorting

import csv

def calculate_efg(fgm, tpm, fga):
    return round(((fgm + 0.5 * tpm) / max(fga, 1)) * 100, 1)

def calculate_impact_score(pts, ast, reb, stl, tov, q4_pts):
    # Weighted metric rewarding playmaking, defense, and 4th-quarter clutch morale
    return round((pts * 1.0) + (ast * 1.8) + (reb * 1.2) + (stl * 2.0) - (tov * 1.5) + (q4_pts * 0.5), 1)

def selection_sort_players(players, key_name):
    # Algorithmic sorting inspired by Harvard CS50x Week 3 (Selection Sort implementation)
    n = len(players)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if players[j][key_name] > players[max_idx][key_name]:
                max_idx = j
        players[i], players[max_idx] = players[max_idx], players[i]
    return players

def run_analytics_report(csv_filepath):
    roster = []
    with open(csv_filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = {k: (int(v) if k != "player_role" else v) for k, v in row.items()}
            p["efg_pct"] = calculate_efg(p["fgm"], p["tpm"], p["fga"])
            p["ast_to"] = round(p["ast"] / max(p["tov"], 1), 2)
            p["impact"] = calculate_impact_score(p["pts"], p["ast"], p["reb"], p["stl"], p["tov"], p["q4_pts"])
            roster.append(p)

    sorted_roster = selection_sort_players(roster, "impact")
    print("=== HIGH SCHOOL BASKETBALL ANALYTICS (3RD PLACE TOURNAMENT RUN) ===")
    for r in sorted_roster:
        print(f"{r['player_role']:22} | eFG%: {r['efg_pct']:5.1f}% | AST/TO: {r['ast_to']:4.2f} | Impact: {r['impact']:5.1f}")

if __name__ == "__main__":
    run_analytics_report("team_match_stats.csv")
