#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-09 12:53
# @Author  : Joe
# @Site    : 
# @File    : demo01_doubanSpider.py
# @Software: PyCharm

import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def get_movie_info(url):
    # url = "https://movie.douban.com/top250"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    # html = str(r.content.decode("utf-8"))
    html = str(r.content.decode("utf-8")).replace('&nbsp;/&nbsp;', '').replace("&#39;", "'")
    soup1 = BeautifulSoup(html, "html.parser")

    item = soup1.find_all("div", attrs={"class": "item"})

    name = []
    director = []
    main_performer = []
    year = []
    content = []
    rating_num = []
    quote = []
    for i in item:
        soup2 = BeautifulSoup(str(i), "html.parser")

        for j in soup2.find_all("a"):
            if j.text == "\n\n":
                pass
            else:
                name.append(j.text[1:-1].replace("\n", " / "))
        for k in soup2.find_all("p", attrs={"class": ""}):
            k_list = k.text[1:-1].strip().split("\n")
            director.append(k_list[0].split(":")[1][:-5].replace("\xa0\xa0", ""))
            try:
                main_performer.append(k_list[0].split(":")[2])
            except BaseException as e:
                main_performer.append("无法显示")
                print(e)
            year.append(k_list[1].strip()[0:4])
            content.append((k_list[1].strip()[6:]))

        for m in soup2.find_all("span", attrs={"class": "rating_num"}):
            rating_num.append(m.text)
        for m in soup2.find_all("p", attrs={"class": "quote"}):
            quote.append(m.text[1:-1])
    time.sleep(np.random.randint(3,6))
    return name, director, main_performer, year, content, rating_num, quote


if __name__ == '__main__':
    page = 10
    movie = []
    movie_name = []
    movie_director = []
    movie_main_performer = []
    movie_year = []
    movie_content = []
    movie_rating_num = []
    movie_quote = []
    for i in range(page):
        url = "https://movie.douban.com/top250?start=" + str(i*25) + "&filter="
        # url="https://movie.douban.com/top250"
        name, director, main_performer, year, content, rating_num, quote = get_movie_info(url)
        movie_name += name
        movie_director += director
        movie_main_performer += main_performer
        movie_year += year
        movie_content += content
        movie_rating_num += rating_num
        movie_quote += quote

    for a, b, c, d, e, f, g in zip(movie_name, movie_director, movie_main_performer, movie_year, movie_content,
                                   movie_rating_num, movie_quote):
        movie_dict = {}
        movie_dict["name"] = a
        movie_dict["director"] = b
        movie_dict["main_performer"] = c
        movie_dict["year"] = d
        movie_dict["content"] = e
        movie_dict["rating_num"] = f
        movie_dict["quote"] = g
        # print(movie_dict)
        movie.append(movie_dict)

    # print(movie)
    df = pd.DataFrame(movie,)
    # df.to_csv("./movie_.csv")

