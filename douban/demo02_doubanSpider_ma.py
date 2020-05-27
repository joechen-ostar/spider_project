import requests,os,re,time
from bs4 import BeautifulSoup


def get_page_info(page=1):

    # https://movie.douban.com/top250?start=25&filter=
    # https://movie.douban.com/top250?start=50&filter=
    url="https://movie.douban.com/top250?start="+str((page-1)*25)+"&filter="
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        "Referer":""
    }
    r=requests.get(url,headers=headers)
    # print(r.text)
    # 讲请求到的网页的源代码存储到文本中,在测试的时候,只需要请求文本网页就可以了
    # with open("douban.html",'w',encoding='utf-8') as file:
    #     file.write(r.text)

    # 先打开本地的网页,做测试,如果代码写好了之后,再用线上的页面
    # with open('douban.html','r',encoding='utf-8') as file:
    #     soup=BeautifulSoup(file.read(),'html.parser')
    soup=BeautifulSoup(r.text,'html.parser')
    movies_li=soup.find("ol",attrs={"class":"grid_view"}).find_all("li")
    # print(movies_li)
    # print(len(movies_li))

    # 创建文件夹用来保存图片
    baseDir="./movies/"
    if os.path.exists(baseDir)==False:
        os.mkdir(baseDir)

    movies=[]
    for li in movies_li:
        img_url=li.find('div',attrs={"class":"pic"}).a.img.attrs['src']
        movie_name=li.find('div', attrs={"class": "pic"}).a.img.attrs['alt']
        # print(movie_name)
        img_r=requests.get(img_url,headers=headers,stream=True)

        with open(baseDir+movie_name+".jpg",'wb') as file:
            for j in img_r.iter_content(10240):
                file.write(j)
        print("%s电影下载成功"%(movie_name))
        info1=li.find("div",attrs={"class":"bd"}).find("p",attrs={"class":""}).text.strip()
        director=info1.split("\n")[0].split("   ")[0][4:]
        # print(director)
        info2=info1.split("\n")[1].strip().split("/")
        movie_year=info2[-3].strip()
        movie_area=info2[-2].strip()
        movie_type=info2[-1].strip()
        # print(movie_year,movie_area,movie_type)
        movie_rating=li.find("span",attrs={"class":"rating_num"}).text
        # print(movie_rating)
        movie_rat_num=li.find(text=re.compile("人评价"))[:-3]
        try:
            movie_intro=li.find('span',attrs={"class":"inq"}).text
        except BaseException:
            movie_intro=""
        movies.append([movie_name,director,movie_year,movie_area,movie_type,movie_rating,movie_rat_num,movie_intro])

    return movies

def saveToFile(movies):
    with open("movies1.txt",'a',encoding='utf-8') as file:
        for once in movies:
            file.write('::'.join(once)+"\n")


for page in range(1,11):
    movies=get_page_info(page)
    # print(movies)
    saveToFile(movies)
    print("%d页加载成功"%(page))
    time.sleep(3)


