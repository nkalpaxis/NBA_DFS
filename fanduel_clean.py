import pandas as pd

players = pd.read_csv("fanduel.csv")

players = players.drop(
    [
        "Id",
        "First Name",
        "Last Name",
        "FPPG",
        "Played",
        "Game",
        "Injury Indicator",
        "Injury Details",
        "Tier",
        "Unnamed: 14",
        "Unnamed: 15",
        "Roster Position",
    ],
    axis=1,
)

players["Nickname"] = players["Nickname"].str.replace("'", "")
players["Nickname"] = players["Nickname"].str.replace(".", "")

players.to_csv("fanduel.csv", index=False)

num_proj = pd.read_csv("projections.csv")

num_proj["Player"] = num_proj["Player"].str.replace("'", "")
num_proj["Player"] = num_proj["Player"].str.replace(".", "")

num_proj.to_csv("projections.csv", index=False)
