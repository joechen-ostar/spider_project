# 房源名称 房源url  平方数 楼层 户型 地铁站距离 室友情况
import requests,re,time,json
from bs4 import BeautifulSoup
import img_test

headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Referer":"http://sh.ziroom.com/z/nl/z3.html"
    }
def get_page_info(page=1):
    url="http://sh.ziroom.com/z/nl/z2.html?p="+str(page)
    # http://sh.ziroom.com/z/nl/z2.html
    # http://sh.ziroom.com/z/nl/z2-u4.html?p=1
    # http://sh.ziroom.com/z/nl/z2-u4.html?p=2
    # http://sh.ziroom.com/z/nl/z2-u4.html?p=3
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    houseList=soup.find_all("li",attrs={"class":"clearfix"})
    # 从源代码中得到 图片的 地址,和偏移量
    # var ROOM_PRICE = {"image":"//static8.ziroom.com/phoenix/pc/images/price/0fcc0d83409c547d3a9d038cc7808fa3s.png","offset":[[4,1,7,8],[3,4,0,8],[3,3,7,8],[4,7,0,8],[3,2,7,8],[4,6,7,8],[3,8,2,8],[4,6,0,8],[3,4,7,8],[4,6,7,8],[3,8,0,8],[4,6,7,8],[3,8,7,8],[4,7,2,8],[4,6,2,8],[4,7,0,8],[3,3,2,8],[3,9,7,8]]};
    data_regx=re.compile("var ROOM_PRICE = (.*?);")
    data=json.loads(data_regx.search(r.text).group(1))
    # 把图片保存到本地,识别,再根据偏移量识别
    with open("1.png",'wb') as file:
        img_r=requests.get("http:"+data['image'],headers=headers,stream=True)
        file.write(img_r.content)
    price_text=img_test.main("1.png")
    print(price_text)
    exit()
    houseInfo=[]
    for once in houseList:
        txt=once.find('div',attrs={"class":"txt"})
        housename=txt.h3.a.string
        houseurl="http:"+txt.h3.a.attrs['href']
        info=re.sub("\s",'',txt.find("div",attrs={"class":"detail"}).p.text).split("|")
        housesquare=info[0]
        housefloor=info[1]
        housetype=info[2]
        houseposition=txt.find("div", attrs={"class": "detail"}).find_all("p")[1].span.string
        # housemate = get_great_roommate(houseurl)
        # houseInfo.append([housename,houseurl,housesquare,housefloor,housetype,houseposition,"-".join(map(lambda x:str(x),housemate.values()))])

    return houseInfo


def get_great_roommate(url):
    print("正在%s房间获取室友数据"%(re.search("/(\d+)\.html",url).group(1)))
    # url="http://sh.ziroom.com/z/vr/60367663.html"
    headers['Referer']="http://sh.ziroom.com/z/nl/z2-u4.html"
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    all_li=soup.find("div",attrs={"class":"greatRoommate"}).find_all("li")
    roommate_num={"man":0,"woman":0,'current':0}
    for once_li in all_li:
        classs=once_li.attrs['class']
        if "man" in classs:
            roommate_num['man']+=1
        elif "woman" in classs:
            roommate_num['woman']+=1
        elif 'current' in classs:
            roommate_num['current']+=1
    time.sleep(1)
    return roommate_num

def saveToFile(houseList):
    with open("ziru_info.txt",'a',encoding='utf-8') as file:
        for once in houseList:
            file.write(",".join(once)+"\n")

def line_check():
    uline=int(input("请输入地铁线路:"))
    ustation=input("请输入地跌站(输入n全部):")
    with open("ziru_info.txt",'r',encoding='utf-8') as file:
        houselist=file.readlines()

    result_list=[]
    for once in houselist:
        regx=re.compile("距(\d+)号线(.*?)站步行约(\d+)米")
        result=regx.search(once)
        info={}
        info['line']=int(result.group(1))
        info['station']=result.group(2)
        info['meter']=int(result.group(3))
        once_list=once.split(',')
        # print(info)
        if ustation=="n":
            if uline==info['line'] :
                result_list.append({"name":once_list[0],"url":once_list[1],'line':info['line'],'station':info['station'],'meter':info['meter'],"roommate":once_list[-1]})
        else:
            if uline==info['line'] and ustation==info['station']:
                result_list.append(
                    {"name": once_list[0], "url": once_list[1], 'line': info['line'], 'station': info['station'],'meter': info['meter'], "roommate": once_list[-1]})

    status=input("请输入要根据那种情况排序,1.距离,2,室友性别")
    if status=='1':
        result_list.sort(key=lambda x:x['meter'])

    elif status=='2':
        sex=input("根据男生还是女生(1男,2女)")
        if sex=="1":
            result_list.sort(key=lambda x:int(x['roommate'].split('-')[0]),reverse=True)
        elif sex=='2':
            result_list.sort(key=lambda x: int(x['roommate'].split('-')[1]), reverse=True)
    for i in result_list:
        print(i)
# for page in range(1,51):
#     houseinfo=get_page_info(page)
#     saveToFile(houseinfo)

# line_check()

get_page_info()