import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
movie_info_list = []
for page in range (1,11):
    url = "https://ssr1.scrape.center/page/%d" %page
    response = requests.get(url,headers=headers)

    if response.status_code==200:
        soup = BeautifulSoup(response.text,"html.parser")
        # print("successful access")
        movies = soup.find_all(name="div",class_="el-card item m-t is-hover-shadow")
        # movie_info_list = []
        for movie in movies:
            movie_info = {}

            movie_name=movie.find(name="h2",class_="m-b-sm")
            if movie_name:
                movie_name = movie_name.text
            else:
                title = "None"
            movie_info["movie_name"] = movie_name

            movie_types = movie.find_all(name="button",class_="el-button category el-button--primary el-button--mini")
            movie_type_all = ""
            for movie_type in movie_types:

                if movie_type and movie_type.span:
                    movie_type = movie_type.span.text
                else:
                    movie_type = "None"
                movie_type_all += movie_type + " "
            movie_info["movie_type"] = movie_type_all

            movie_small_groups = movie.find_all(name="div", class_="m-v-sm info")
            movie_small_groups_all = []
            for movie_small_group in movie_small_groups:
                span_list = movie_small_group.find_all(name="span")
                for s in span_list:
                    s=s.text
                    if s != " / ":
                        movie_small_groups_all.append(s)

            # print(movie_small_groups_all)
            if len(movie_small_groups_all) >= 1:
                movie_country = movie_small_groups_all[0]
                movie_info["movie_country"] = movie_country
            if len(movie_small_groups_all) >= 2:
                movie_length = movie_small_groups_all[1]
                movie_info["movie_length"] = movie_length
            if len(movie_small_groups_all) >= 3:
                movie_release_date = movie_small_groups_all[-1]
                movie_info["movie_release_date"] = movie_release_date
            else:
                movie_info["movie_release_date"] = "None"

            movie_rating = movie.find(name="p", class_="score m-t-md m-b-n-sm")
            if movie_rating:
                movie_rating = movie_rating.text.strip()
            else:
                movie_rating = "None"
            movie_info["movie_rating"] = movie_rating

            movie_info_list.append(movie_info)
        print(movie_info_list)

    else:
        print("cannot access")
df = pd.DataFrame(movie_info_list)
df.to_csv("scrape_movie_all.csv", index = False)
