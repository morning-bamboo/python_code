import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://la28.org/en/games-plan/olympics.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text,"html.parser")
games = soup.find_all(name = "li", class_ = "list-item")
game_datalist = []
for game in games:
    game_info = {}
    game_title = game.find("span",class_ = "list-item-title")
    if game_title:
        game_title = game_title.text
    else:
        game_title = "None"
    # print(game_title)

    game_link = game.a["href"]
    # for game_link in game_links:
    #     href = game_link.get("href")
    game_url = "https://la28.org" + game_link
    # print(game_url)
    game_info["game_title"] = game_title
    game_info["game_link"] = game_url.strip()
    # print(f"Game Title: {game_title}  {game_url}")
    game_datalist.append(game_info)
# print(game_datalist)

#write into csv
game_df = pd.DataFrame(game_datalist)
game_df.to_csv("LA28Games.csv", index=False)

#re-read from the saved csv
df2 = pd.read_csv("LA28Games.csv")
print(df2.describe())

