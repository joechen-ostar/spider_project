import requests, re, time, os
from bs4 import BeautifulSoup
import json
import urllib
import numpy as np


# 输入城市和职位名称 下载数据
def get_position_info(city, position):
    url_homePage = "https://www.lagou.com/jobs/list_" + str(position) + "?&px=default&city=" + city + "#filterBox"
    url_json = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=" + urllib.parse.quote(
        city) + "&needAddtionalResult=false"
    referer = "https://www.lagou.com/jobs/list_" + str(position) + "?&px=default&city=" + urllib.parse.quote(city)

    headers_json = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Host": "www.lagou.com",
        "Origin": "https://www.lagou.com",
        "Referer": referer
    }

    headers_homepage = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Host": "www.lagou.com"
    }

    sess = requests.Session()
    sess.get(url_homePage, headers=headers_homepage)
    startRound = 100
    while startRound < 1000:
        for page in range(startRound, startRound + 10):
            if page == 1:
                flag = True
            else:
                flag = False

            form_data = {
                "first": flag,
                "pn": page,
                "kd": position
            }

            r = sess.post(url_json, headers=headers_json, data=form_data)

            # 将json下载到本地，避免频繁的访问 被限制
            # with open("./a.text", "w", encoding="utf-8") as file:
            #     file.write(r.text)
            # with open("./a.text", "r", encoding="utf-8") as file:
            #     json_str = file.read()

            json_dict = json.loads(r.text)

            position_list = []
            for i in json_dict["content"]["positionResult"]["result"]:
                positionName = i["positionName"]
                companyId = i["companyId"]
                companyFullName = i["companyFullName"]
                companySize = i["companySize"]
                industryField = i["industryField"]
                financeStage = i["financeStage"]
                firstType = i["firstType"]
                secondType = i["secondType"]
                thirdType = i["thirdType"]
                createTime = i["createTime"]
                city = i["city"]
                district = i["district"]
                salary = i["salary"]
                workYear = i["workYear"]
                jobNature = i["jobNature"]
                education = i["education"]
                temp_list = [positionName, companyId, companyFullName, companySize, industryField, financeStage,
                             firstType, secondType, thirdType, createTime, city, district, salary, workYear, jobNature,
                             education]
                for j in range(15):
                    temp_list[j] = str(temp_list[j])
                position_list.append(temp_list)
            download_position_info(position_list)
            print("正在下载第%d页" % (page))
        startRound += 10
        time.sleep(60+np.random.randint(20,50))


# 输入职位列表下载到本地
def download_position_info(position_list):
    with open("./position_info000000.text", "a", encoding="utf-8") as file:
        for once in position_list:
            file.write("::".join(once) + "\n")


if __name__ == '__main__':
    get_position_info("北京", 'python')
