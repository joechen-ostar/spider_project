import re,requests,json,time
from download_Tools import download_img
# 静态网站
# 1. 请求网页得到源代码
# 2. 使用正则 匹配到想要的内容

# 请求源代码,发现源代码中根本没有 图片 <img
# url="http://pic.gamersky.com/cos/"
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
#     "Referer":"http://pic.gamersky.com/bz/"
# }
# r=requests.get(url,headers=headers)
# print(r.content.decode('utf-8'))


# 网页中的所有元素都可以在network中找到,如果源代码中找不到的话,有可能是动态请求得到的, 所以我们要在network中找
# 小tips , network中的 XHR(XmlHttpRequest) 中可以查询到大部分网站的动态请求,但是有的网站动态请求在xhr找不到,只能在all里面查找
# response 是返回值
# preview 是解析过的返回值

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
        "Referer":"http://pic.gamersky.com/cos/"
    }

# 在network中找到了一个链接,返回的是我们的图片的一些信息
def get_series_list():
    url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=1&pageSize=50&nodeId=21093"
    # http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=1&pageSize=50&nodeId=21093
    # http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=2&pageSize=50&nodeId=21093
    # http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=3&pageSize=50&nodeId=21093

    r=requests.get(url,headers=headers)
    # 解析了一次之后,发现还是一个字符串,发现区别是,这次请求的带有反斜线还有最外层的双引号,是做了两次转换
    result=json.loads(json.loads(r.text))

    # print(result)
    # print(type(result))
    # print(result['totalCount'])
    info=[]
    for once in result['body']:
        title=re.sub("[/\\\\><\*\?\":]",'',once['title'])
        info.append({"name":title,"url":once['path']})

    return info


def get_once_series_info(url):
    genID=url.split('.')[-2].split('/')[-1]
    url="http://pic.gamersky.com/home/getimages?jsondata=%7B%22generalId%22%3A%22"+genID+"%22%2C%22sort%22%3A%22hot_desc%22%2C%22pageIndex%22%3A1%2C%22pageSize%22%3A50%2C%22gameId%22%3A%220%22%2C%22tagId%22%3A%220%22%7D"
    # url="http://pic.gamersky.com/home/getimages?jsondata=%7B%22generalId%22%3A%22891887%22%2C%22sort%22%3A%22hot_desc%22%2C%22pageIndex%22%3A1%2C%22pageSize%22%3A50%2C%22gameId%22%3A%220%22%2C%22tagId%22%3A%220%22%7D"
    # url="http://pic.gamersky.com/home/getimages?jsondata=%7B%22generalId%22%3A%22897862%22%2C%22sort%22%3A%22hot_desc%22%2C%22pageIndex%22%3A1%2C%22pageSize%22%3A50%2C%22gameId%22%3A%220%22%2C%22tagId%22%3A%220%22%7D"
    # 对比每个动态请求的链接地址,发现不同点是 generalId,应该是系列的编号,可以从url中切出来
    # print(url)
    # 每一次请求的Referer就是该系列的链接地址
    headers['Referer']=url
    r=requests.get(url,headers=headers)
    result=json.loads(json.loads(r.text))
    img_list=[]
    for once in result['body']:
        img_list.append(once['originImg'])
    return img_list




seriesinfo=get_series_list()
# print(len(seriesinfo))
for once in seriesinfo:
    imglist=get_once_series_info(once['url'])
    download_img(imglist,once['name'])
    time.sleep(3)