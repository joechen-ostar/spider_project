#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-05 11:57
# @Author  : Joe
# @Site    : 
# @File    : demo1_爬取视频.py
# @Software: PyCharm

import datetime
import requests
import json
def get_ts_url(m3u8_path, root_url):
    urls = []
    with open(m3u8_path, 'r') as fhand:
        lines = fhand.readlines()
        for line in lines:
            if line.endswith('.ts\n'):
                urls.append(root_url + line.strip('\n'))
    # print(urls)
    return urls



def download_ts(ts_urls, download_path):
    for i in range(len(ts_urls)):
        ts_url = ts_urls[i]
        file_name = ts_url.split('/')[-1]
        print('start download %s' % file_name)
        start = datetime.datetime.now().replace(microsecond=0)
        try:
            response = requests.get(ts_url, stream=True)
        except Exception as e:
            print('Error prosessed: %s' % e )
            return
        ts_path = download_path + '/{0}.ts'.format(i)
        with open(ts_path, 'wb+') as fhand:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:
                    fhand.write(chunk)
        end = datetime.datetime.now().replace(microsecond=0)
        print('Time cost: %s' % (end - start))

def download_key(m3u8_path, root_url):
    url = ''
    with open(m3u8_path, 'r') as fhand:
        lines = fhand.readlines()
        for line in lines:
            if line.startswith('#EXT-X-KEY'):#line.endswith('key.key\"/n'):
                print(line)
                url = line.split(',')[-1].split('\"')[-2] # .split('"')[-1]
                break
    key_url = root_url + url
    file_name = key_url.split('/')[-1]
    res = requests.get(key_url)
    file_path = './'+file_name
    with open(file_path, 'wb') as fhand:
         fhand.write(res.content)
    return file_path

def get_pid():
    return 'pid-1-5-1'


def get_token():
    # 这个是获取广告的token
    # token_url = 'https://edu.csdn.net/bcscloud/course_video/get_start_token?url='+guanggao_url
    # return json.loads(requests.get(token_url).text).get('token')

    # 后边的/10085/215004是在网页地址栏里，没办法，手工获取吧
    # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    #     "Referer": "http://tpcst.ibeifeng.com/Video/CourseVideo/911115dd-9956-419a-9ed1-d08193004dec?chapterName=Python%E9%AB%98%E7%BA%A7%E7%88%AC%E8%99%AB-%E9%A9%AC%E7%BA%A2%E8%BF%90%E8%80%81%E5%B8%88&courseName=AI%E5%B0%B1%E4%B8%9A%E4%BA%8C%E5%8D%81%E4%B8%80%E7%8F%AD%E5%91%A8%E6%9C%AB%E5%BD%95%E5%B1%8F&sectionId=42d21773-d376-4bc7-b7be-21d06a5b03db"
    # }
    # login_url="http://authcenter.ibeifeng.com/core/login?signin=be00d1294002392442ed853d02fd65e9&type=1"
    # data={
    #     "__RequestVerificationToken": "jlU7fjtLrs_iMRS8Ai9obibRHGDHZ8PWES8rxZmoR4B1QuI5 - M_04cpgO_pyH0BoDzCvyE9FXnkE6SB12YUNIE4UKSI1",
    #     "idsrv.xsrf": "MliRpCf1JK1JkQ9c7JPYwshPWBYHd5c3Ezj0XxkOUXJqDd09bturUnZc5VoJk0zRyzZYHYjL7qWDbcrhJhOAQ1SrZJU",
    #     "thisserverappname": "237AuthCenterWebApi",
    #         "UserName": "teacher_chenzhiqiang",
    # "Password": "(*)Ibeifeng666",
    # "Code": "",
    # "Phone": "",
    # "PhoneCode": "",
    # "LoginType": 1
    # }
    # s=requests.session()
    # r=s.post(login_url,data=data,headers=headers)
    # print(r.text)
    #
    # token_url = 'http://tpcst.ibeifeng.com/Video/GetVideoToken'
    # data={"mediaId": "mda-jjrqeryjayk938si"}
    # print(s.post(token_url,data=data,headers=headers).text)
    return "5576b842db4075047b635135d595fb6dd0199f8f99cc32766a507a78bf1f1b39_cc08e89f8aa14961a77f0647fc7759e1_1575541410"





def get_key(key_url):
    key_url_all = key_url+'&playerId='+get_pid()+'&token='+get_token()
    print(json.loads(requests.get(key_url_all).text).get('encryptedVideoKey'))
    return json.loads(requests.get(key_url_all).text).get('encryptedVideoKey')



if __name__=="__main__":

    # urls_list=get_ts_url("/Users/a1/Desktop/beifeng_archive/python高级/项目/爬视频/ibeifeng/mda-jjrqeryjayk938si.m3u8","http://gg4gicayym6ymaadxbx.exp.bcevod.com//mda-jjrqeryjayk938si/")
    # download_ts(urls_list,"./raw_video/")
    # download_key("/Users/a1/Desktop/beifeng_archive/python高级/项目/爬视频/ibeifeng/mda-jjrqeryjayk938si.m3u8","https://drm.media.baidubce.com/v1")
    get_key("https://drm.media.baidubce.com/v1/tokenVideoKey?videoKeyId=mda-jjrqeryjayk938si")



