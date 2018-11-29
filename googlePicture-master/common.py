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
    try:
        # 设置20秒timeout
        picture = requests.get(url=url, headers=headers, timeout=20)
        # 写入文件
        filePath = str(name)+str(type)
        f = open(filePath, 'wb')
        try:
            f.write(picture.content)
            f.close()
        except:
            os.remove(filePath)
    except:
        print('下载超时')
        # if(os.path.isfile(filePath)):
        #     os.remove(filePath)
# 解决url中的转义
def urlCode(str):
    str = str.replace('\\u003d','=')
    str = str.replace('\\u0026','&')
    return str

if __name__ == '__main__':
    url = 'http://pop.nosdn.127.net/92eff3d4-2bfa-4212-b61e-638fa2a3f60a.jpg?imageView\u0026thumbnail=400x400'
    print(url)
    url2 = urlCode(url)
    print(url)
    print(url2)
    text =requests.get(url).content
    text = text.decode()
    print(text)
