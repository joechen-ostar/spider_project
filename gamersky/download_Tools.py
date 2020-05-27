import os,requests
def download_img(imglist,series_name):
	basedir="./images/"
	if os.path.exists(basedir) == False:
		os.mkdir(basedir)
	savedir=basedir+series_name+'/'
	if os.path.exists(savedir)==False:
		os.mkdir(savedir)
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",

	}
	print("现在要下载的系列为:%s,总图片个数为%d张"%(series_name,len(imglist)))
	index=0
	for once_img in imglist:
		img_r=requests.get(once_img,headers=headers,stream=True)
		savepath=savedir+"%d.jpg"%(index)
		with open(savepath,'wb') as file:
			for j in img_r.iter_content(10240):
				file.write(j)
		index+=1
		print("     第%d张图片下载成功"%(index))

