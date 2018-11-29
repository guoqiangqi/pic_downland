import os,threading,time,requests

# 创建文件夹 用来存放图片
def makedir(dirname):
    if os.path.lexists(dirname):
        os.chdir(dirname)
    else:
        os.makedirs(dirname)
        os.chdir(dirname)

#         每秒打印线程数目
def pringThreadNumberEverySecond():
    while(threading.activeCount()>1):
        print(str(threading.activeCount()) + 'actived thread')
        time.sleep(1)

#  图片下载
def downloadPicture(url,name,type):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'}
    # 设置20秒timeout
    picture = requests.get(url=url, headers=headers, timeout=20)
    # 写入文件
    f = open(str(name) + str(type), 'wb')
    f.write(picture.content)
    f.close()
