#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-21 23:08
# @Author  : Joe
# @Site    : 
# @File    : proxy_text.py
# @Software: PyCharm
import requests,random

proxies_list=[]
with open('./proxies_.txt','r',encoding='utf-8') as file:
    #print(file.readline())

    while True:
        txt=file.readline().strip('\n').strip('\ufeff')
        if txt=='':
            break
        proxies_list.append(txt)
    # print(proxies_list)

url='http://httpbin.org/ip'
proxies_1=random.choice(proxies_list)

proxies={'http':proxies_1}
print(proxies)
r=requests.get(url,proxies=proxies)
print(r.text)
