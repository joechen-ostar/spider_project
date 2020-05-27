import requests,re,os,time
from lxml import etree


url="http://sh.baletu.com/zhaofang/?entrance=14"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    "Referer":"http://www.baletu.com/"
}
r=requests.get(url,headers=headers)
html=etree.HTML(r.text)
house_li=html.xpath("//div[@class='list-center']/ul/li")
# print(house_li)
# print(len(house_li))
for once in house_li:
    title=once.xpath(".//h3/a/@title")[0]
    village=once.xpath("./@name")[0]
    price=once.xpath("./@price")[0]
    variant=once.xpath("./@variant")[0]
    area=title.split(" ")[0].split("-")[-1]
    info1=once.xpath(".//p[@class='list-pic-ps']/span[2]/text()")[0]
    type=info1.split("|")[1]
    square=info1.split("|")[-1]
    # print(type,square)
    addtime=once.xpath(".//span[@class='room-time']/text()")[0][:-3]
    # print(addtime)
    info2=once.xpath(".//div[@class='list-pic-ad']/text()")[0]
    print(info2)
    # 距离3号线大柏树地铁站340米
    # 距离2号线徐泾东地铁站1054米
    try:
        regex=re.compile("距离(?:(\d+)号线)?(.*?)(?:地铁站|公交站)(\d+)米")
        res=regex.search(info2).groups()
        line=res[0]
        station=res[1]
        meter=res[2]
    except BaseException:
        line=None
        station=info2
        meter=None
    print(line,station,meter,sep="---")
    # break

