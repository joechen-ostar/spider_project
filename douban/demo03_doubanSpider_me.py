#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-10 12:01
# @Author  : Joe
# @Site    : 
# @File    : demo03_doubanSpider_me.py
# @Software: PyCharm

import requests, os,time
from bs4 import BeautifulSoup


#

#
# r = requests.get(url, headers=headers)
#
# with open("./douban_250.html","w",encoding="utf-8") as file:
#     file.write(r.text)
#
# with open("./douban_250.html", "r", encoding="utf-8") as file:
#     douban_250_html = file.read()
#
# soup = BeautifulSoup(douban_250_html, "html.parser")
#
# ol_item = soup.find('ol', attrs={"class": "grid_view"})


def download_image(url, name):
    baseDir = "./image/"
    if os.path.exists(baseDir) == False:
        os.makedirs(baseDir)
    saveDir = baseDir + name + ".jpg"

    with open(saveDir, "wb") as file:
        r = requests.get(url, headers=headers)
        for i in r.iter_content(10240):
            file.write(i)


def download_movie_info(movie_list):
    with open("./movie_info.text", "a", encoding="utf-8") as file:
        for once in movie_list:
            file.write("::".join(once) + "\n")


def get_movie_content(url, headers):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    ol_item = soup.find('ol', attrs={"class": "grid_view"})
    movie_list = []
    for i in ol_item.find_all("li"):
        img_url = i.img.attrs["src"]
        img_name = i.img.attrs["alt"]
        download_image(img_url, img_name)
        director = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[0].split("   ")[0][4:]
        try:
            main_performer = \
                i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[0].split("   ")[1].split(":")[1]
        except BaseException:
            main_performer = ""

        year = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[1].strip().split("/")[0].strip()
        region = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[1].strip().split("/")[1].strip()
        content = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[1].strip().split("/")[2].strip()
        rating_star = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[5]
        rating_num = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[7][:-3]
        quote = i.find("div", attrs={"class": "bd"}).text.strip().split("\n")[10]
        # movie_list.append({
        #     "img_name": img_name,
        #     "director": director,
        #     "year": year,
        #     "region": region,
        #     "content": content,
        #     "rating_star": rating_star,
        #     "rating_num": rating_num,
        #     "quote": quote})
        movie_list.append([img_name, director, year, region, content, rating_star, rating_num, quote])
    # print(movie_list)
    download_movie_info(movie_list)


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    page = 10
    for i in range(page):
        url = "https://movie.douban.com/top250?start=" + str(i * 25) + "&filter="
        get_movie_content(url, headers)
        time.sleep(5)
        print("------------正在下载第%d页电影信息------------"%(i))
