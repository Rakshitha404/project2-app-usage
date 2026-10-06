import pandas as pd
import numpy as np
data = pd.read_csv("day02_usage.csv")
chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()
print(len(chat))
print("Chat total:", chat.sum())
print("Chat average:", round(chat.mean(), 1))

print("Video total:", video.sum())
print("Video average:", round(video.mean(), 1))

print("Study total:", study.sum())
print("Study average:", round(study.mean(), 1))

print("Games total:", games.sum())
print("Games average:", round(games.mean(), 1))
study_games = study - games
best_position = np.argmax(study_games)
worst_position = np.argmin(study_games)
print("Best day:", best_position + 1)
print("Worst day:", worst_position + 1)
apps = ["Chat", "Video", "Study", "Games"]

for i in range(30):
    values = [chat[i], video[i], study[i], games[i]]
    winner_position = np.argmax(values)
    print("Day", i + 1, ":", apps[winner_position])
    total = chat + video + study + games

chat_percent = chat / total * 100
video_percent = video / total * 100
study_percent = study / total * 100
games_percent = games / total * 100
print(chat_percent)
print(video_percent)
print(study_percent)
print(games_percent)