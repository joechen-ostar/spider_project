#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-21 19:21
# @Author  : Joe
# @Site    : 
# @File    : lagou_spider_demo2.py
# @Software: PyCharm

import requests
import pandas
import time
import random
import urllib

#用于获取页面信息
def getWebResult(url,cookies,form,header,proxies):
    html = requests.post(url=url,cookies=cookies,data=form, headers=header, proxies=proxies)
    result = html.json()
    #找到html中result包含的招聘职位信息
    # print(result)
    data = result['content']['positionResult']['result'] # 返回结果在preview中的具体返回值
    return data

#将招聘信息按照对应的参数，组装成字典
def getGoalData(data):
    for i in range(15):#每页默认15个职位
        info={
            'positionName': data[i]['positionName'],    #职位简称
            'companyShortName': data[i]['companyShortName'],    #平台简称
            'salary': data[i]['salary'],    #职位薪水
            'createTime': data[i]['createTime'],    #发布时间
            'companyId':data[i]['companyId'],   #公司ID
            'companyFullName':data[i]['companyFullName'],   #公司全称
            'companySize': data[i]['companySize'],  #公司规模
            'financeStage': data[i]['financeStage'],    #融资情况
            'industryField': data[i]['industryField'],  #所在行业
            'education': data[i]['education'],  #教育背景
            'district': data[i]['district'],    #公司所在区域
            'businessZones':data[i]['businessZones']    #区域详细地
        }
        data[i]=info
    return data

#保存data至csv文件
def saveData(data,stage):
    table = pandas.DataFrame(data)
    table.to_csv(r'./data/LaGou_quanguo.csv', header=stage, index=False, mode='a+')

def get_proies_list():
    proxies_list=[]
    with open('./proxies_2.txt', 'r', encoding='utf-8') as file:
        # print(file.readline())

        while True:
            txt = file.readline().strip('\n').strip('\ufeff')
            if txt == '':
                break
            proxies_list.append(txt)
    return proxies_list

def main():
    url1 = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
    # 职位关键字
    job = 'python'

    # 职位所属地
    city = '武汉'
    # 模拟请求的url
    # url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=' + urllib.parse.quote(city) + '&needAddtionalResult=false'
    url_quanguo='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    # print(url1)

    # 拼装header信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Referer': 'https://www.lagou.com/jobs/list_python/p-city_9?px=default',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Host': 'www.lagou.com'
        }
    # s = requests.Session()  # 建立session
    # s.get(url=url1, headers=headers, timeout=10)
    # print(s.get(url=url1, headers=headers, timeout=10).text)
    # cookies = s.cookies  # 获取cookie
    # cookies = {
    #     'Cookie':' _ga=GA1.2.1499991452.1534085805; user_trace_token=20180812225645-ee28a588-9e3f-11e8-a37b-5254005c3644; LGUID=20180812225645-ee28aac6-9e3f-11e8-a37b-5254005c3644; WEBTJ-ID=20180927222225-1661b68d0a37-0b11bfd97d0f95-346a7809-1296000-1661b68d0a47da; _gid=GA1.2.150811619.1538058146; X_HTTP_TOKEN=7ef120203302eaa5cd2d6f14f01d94b8; LG_LOGIN_USER_ID=210fc6122b83eb29927899e722463f91536920a7b853cd6c; _putrc=C259D6000DA09FDE; JSESSIONID=ABAAABAAAGFABEF00AF5692AF9B9D2C66B07270E514B7A9; login=true; unick=%E5%B0%9A%E5%85%A8%E9%91%AB; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=26; index_location_city=%E5%8C%97%E4%BA%AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538058189,1538137263,1538231886,1538298276; gate_login_token=e052ef59f765dd0dc8e68637d17b953008d587077d8a7f78; TG-TRACK-CODE=search_code; LGSID=20180930224915-006ea101-c4c0-11e8-bb68-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E4%25BA%25A7%25E5%2593%2581%25E7%25BB%258F%25E7%2590%2586%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; SEARCH_ID=3dd73994b82a47be86797e1f001db6c6; _gat=1; LGRID=20180930231820-109f3a78-c4c4-11e8-bb68-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538320700'
    # }

    #用于定义开始爬取的起始页码
    startPage=1

    #拉勾网有个限制，单次只能连续爬取5页，所以使用一个以5页为轮循的小策略
    while startPage<1000:
        # 获取随机ip
        # proxies_1 = random.choice(get_proies_list())
        # proxies = {'http': proxies_1}
        # s = requests.Session()
        # s.get(url=url1, headers=headers, proxies=proxies, timeout=10)
        # cookies = s.cookies
        for i in range(startPage, startPage+10):
            proxies_1 = random.choice(get_proies_list())
            proxies = {'http': proxies_1}
            s = requests.Session()
            s.get(url=url1, headers=headers, proxies=proxies, timeout=10)
            cookies = s.cookies
            #拼装Form Data信息
            if i == 1:
                flag = 'true' #当是首次请求时，使用flag=true标志
                stage = True  #stage是用来标示csv是否创建表头的参数，仅在第一次保存数据时创建
            else:
                flag = 'false'
                stage = False
            num = i
            form = {'first': flag,  # 标示是否是首次请求标示，第二页以后则为false
                    'kd': job,
                    'pn': str(num)}
            print('------page %s-------' % i) #打印当面爬取的页码
            #调用函数，获取相应的招聘信息
            data = getWebResult(url_quanguo,cookies,form, headers,proxies)
            #调用函数，拼装招聘信息
            data_goal = getGoalData(data)
            #调用函数，保存info数据
            saveData(data_goal, stage)
        #以10页为单次，依次轮循
        startPage+=10
        #休眠一定时间
        # time.sleep(60+random.randint(10,50))


if __name__ == '__main__':
    main()

