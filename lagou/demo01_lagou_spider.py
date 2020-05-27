import requests,json,urllib
url='https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
headers={
'Referer': 'https://www.lagou.com/jobs/list_python/p-city_2?px=default',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
'Host': 'www.lagou.com',
'Accept': 'application/json, text/javascript, */*; q=0.01'
}
form={
'first': 'true',
'pn': 1,
'kd': 'python'
}
headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Referer': 'https://www.lagou.com/jobs/list_python/p-city_9?px=default',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Host': 'www.lagou.com'
        }
# url2 = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
url2 = 'https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput='
s = requests.Session()
s.get(url=url2, headers=headers2, timeout=10)
cookies = s.cookies
html = requests.post(url=url,data=form,headers=headers,cookies=cookies)
# result = html.json()
print(html.text)



