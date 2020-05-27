#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-21 12:45
# @Author  : Joe
# @Site    : 
# @File    : lagou_spider.py
# @Software: PyCharm

import requests
# import codecs
from urllib import request,parse
# url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
#
# headers={
# "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36","Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="}
#
# my_headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
# 'Host':'www.lagou.com',
# 'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
# 'X-Anit-Forge-Code':'0',
# 'X-Anit-Forge-Token': 'None',
# 'X-Requested-With':'XMLHttpRequest' }
# my_headers2={
# "Accept": "application/json, text/javascript, */*; q=0.01",
# "Accept-Encoding": "gzip, deflate, br",
# "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
# "Connection": "keep-alive",
# "Content-Length": "25",
# "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
# "Cookie": "JSESSIONID=ABAAABAAAFCAAEG048EDD8D85672237AD79D13ACEDCB240; WEBTJ-ID=09212019%2C124541-16d5223d0493c7-080b39a5a176fd-38607501-1296000-16d5223d04d75a; _ga=GA1.2.952226443.1569041142; _gid=GA1.2.1869307686.1569041142; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1569041142; user_trace_token=20190921124542-aac78e76-dc2a-11e9-946a-525400f775ce; LGSID=20190921124542-aac78f93-dc2a-11e9-946a-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190921124542-aac7914a-dc2a-11e9-946a-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=f0f504af054476e2641140965189b72e69ac80822a; LGRID=20190921124551-b011c2ca-dc2a-11e9-a524-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1569041151; TG-TRACK-CODE=search_code; SEARCH_ID=fc5f09bed8924963b980f2363ab76f0d",
# "Host": "www.lagou.com",
# "Origin": "https://www.lagou.com",
# "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
# "Sec-Fetch-Mode": "cors",
# "Sec-Fetch-Site": "same-origin",
# "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
# "X-Anit-Forge-Code": "0",
# "X-Anit-Forge-Token": "None",
# "X-Requested-With": "XMLHttpRequest"
# }

# city = "上海"
# position = "python"
#
# headers3={
# "Referer": "https://www.lagou.com/jobs/list_{}?city={}&cl=false&fromSearch=true&labelWords=&suginput=".format(codecs.encode(position, 'utf-8'), codecs.encode(city, 'utf-8')),
# "Cookie": "_ga=GA1.2.2138387296.1533785827; user_trace_token=20180809113708-7e257026-9b85-11e8-b9bb-525400f775ce; LGUID=20180809113708-7e25732e-9b85-11e8-b9bb-525400f775ce; index_location_city=%E6%AD%A6%E6%B1%89; LGSID=20180818204040-ea6a6ba4-a2e3-11e8-a9f6-5254005c3644; JSESSIONID=ABAAABAAAGFABEFFF09D504261EB56E3CCC780FB4358A5E; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534294825,1534596041,1534596389,1534597802; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534599373; LGRID=20180818213613-acc3ccc9-a2eb-11e8-9251-525400f775ce; SEARCH_ID=f20ec0fa318244f7bcc0dd981f43d5fe",
#  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36"
# }


# data={
# "first": "true",
# "pn": 1,
# "kd": "python"}

# data2={
# "first": "false",
# "pn": 2,
# "kd": "python",
# "sid": "49037b8d30fc4bf0b745fec270b984a4"
# }
#

#
# response=request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
# resp=request.urlopen(response)
# print(resp.read().decode('utf-8'))


# r=requests.post(url, headers=headers, data=data)
# print(r.text)

import requests
import time
import json


def main(pages):
    # 主url
    url1 = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
    url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

    # ajax请求
    url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_2?px=default',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Host': 'www.lagou.com'
    }
    # 通过data来控制翻页

    for page in range(1, pages):
        data = {
            'first': 'false',
            'pn': page,
            'kd': 'python'
        }
        s = requests.Session()  # 建立session
        s.get(url=url1, headers=headers, timeout=5)
        cookie = s.cookies  # 获取cookie
        response = s.post(url=url, headers=headers, data=data, cookies=cookie, timeout=3)
        info=json.loads(response.text)
        info['content']['positionResult']['result']
        print(info)
        # time.sleep(7)



main(2)