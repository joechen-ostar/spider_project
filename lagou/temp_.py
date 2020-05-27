#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-10 17:48
# @Author  : Joe
# @Site    : 
# @File    : temp_.py
# @Software: PyCharm
#
#
# python 深圳 page=1
#
# "https://www.lagou.com/jobs/list_python/p-city_215?&cl=false&fromSearch=true&labelWords=&suginput="
#
# form_data
#
# first: true
# pn: 1
# kd: python
#
# "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
#
#
# "https://www.lagou.com/jobs/list_python/p-city_215?&cl=false&fromSearch=true&labelWords=&suginput="
#
#
# python 深圳 page=2
#
#
# "https://www.lagou.com/jobs/list_python/p-city_215?&cl=false&fromSearch=true&labelWords=&suginput="
#
#
# first: false
# pn: 2
# kd: python
# sid: 1af9350da0054badbc28baaeddbe9712
#
# "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
#
# "https://www.lagou.com/jobs/list_python/p-city_215?&cl=false&fromSearch=true&labelWords=&suginput="
#
# https://www.lagou.com/jobs/list_python?&px=default&city=%E5%8C%97%E4%BA%AC
#
#
# https://www.lagou.com/jobs/list_python?&px=default&city=安康#filterBox
#
#
# position="python"
# city="北京"
#
# homePage_url="https://www.lagou.com/jobs/list_"+str(position)+"?&px=default&city="+city+"#filterBox"
# url_json="https://www.lagou.com/jobs/positionAjax.json?px=default&city="+urllib.parse.quote(city)+"&needAddtionalResult=false"
# refer="https://www.lagou.com/jobs/list_"+str(position)+"?&px=default&city="+urllib.parse.quote(city)
#
# for page in range(1,20)
#     if page=1
#         first=True
#     else:
#         first=False
#
#     form_data={
#         "first": first,
#         pn: page,
#         kd: position
#      }
#

