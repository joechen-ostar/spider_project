import requests,re
from bs4 import BeautifulSoup
# 爬取 https://www.xicidaili.com/wt 页面中所有的代理数据
# 要爬取的有 ip,端口,服务器地址,是否匿名,类型,存活时间,验证时间
def get_info():
    url="https://www.xicidaili.com/wt"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
        "Referer":"https://www.xicidaili.com/"
    }
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    all_tr=soup.find("table",attrs={"id":"ip_list"}).find_all("tr")[1:]
    agent_list=[]
    for once in all_tr:
        info=once.find_all("td")
        ip=info[1].string
        port=info[2].string
        try:
            position=info[3].a.string
        except BaseException as e:
            position="暂无"
        isanonymous=info[4].string
        htype=info[5].string
        alive_time=info[8].string
        check_time=info[9].string
        agent_list.append({'ip':ip,'port':port,'position':position,'isanonymous':isanonymous,'htype':htype,"alive_time":alive_time,'check_time':check_time})
    return agent_list


def saveToFile(agent_list):
    agent_list=map(lambda x:','.join(x.values())+"\n",agent_list)
    with open("agent_list.txt",'w',encoding="utf-8") as file:

        file.writelines(agent_list)


def check_isuseful():
    with open("agent_list.txt" ,'r',encoding='utf-8') as file:
        agent_list=file.readlines()
    agent_list=map(lambda x:x.strip().split(","),agent_list)
    # print(list(agent_list))
    for once in agent_list:
        print("正在检测%s:%s"%(once[0],once[1]))
        url="http://httpbin.org/get"
        proxies={
            "http":once[0]+":"+once[1]
        }
        try:
            r=requests.get(url,proxies=proxies,timeout=5)
        except BaseException as e:
            once.append("不可用")
        else:
            once.append("可用")
            print(once)

# list1=get_info()
# print(len(list1))
# saveToFile(list1)

check_isuseful()

