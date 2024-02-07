from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
empire_site_data = response.text

soup = BeautifulSoup(empire_site_data, "html.parser")
# print(soup.find(name="h3", class_="title"))

# Getting all the titles in the list
title_list = soup.find_all(name="h3", class_="title")

# Reversing the list to print from 1-100
title_list.reverse()

with open("a.txt", "w", encoding='utf-8') as file:
    for movieTitle in title_list:
        # print(movieTitle.text)
        content = movieTitle.text
        file.write(content + '\n')
