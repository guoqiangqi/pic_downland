import re,requests,os

#B站封面批量获取
print(u"B站封面批量获取,输入开始和截止av号自动下载[开始av号,截止av号)封面")
number1=input("输入开始av号（例如：20035622）:")
number2=input("输入截止av号（例如：20035630）:")
#确定保存目录
if os.path.lexists("bilibili"):
    os.chdir("bilibili")
else:
    os.mkdir("bilibili")
    os.chdir("bilibili")

def download(number1,number2):

    for number in range(int(number1),int(number2)):
        base_url="https://www.bilibili.com/video/av"
        # base_http="http:"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
        url=base_url+str(number)
        # print(url)
        text=requests.get(url,headers=headers).text
        # print(text)
        # 重新定义正则表达式来寻找封面直链
        pattern = re.compile(r'itemprop="image" content="(.*?)"/>', re.S)
        picture=re.findall(pattern,text)
        # print(picture)
        if picture:#视频地址存在
            for i in picture:
                if(i):#封面存在
                    # http=base_http+str(i)
                    http = i
                    #print(http)#图片地址
                    print('正在下载:av'+ str(number) +'正在自动保存在当前页bilibili目录下')

                    try:
                        pic = requests.get(http, timeout=10)
                    except requests.exceptions.ConnectionError:
                        print('【连接超时】当前图片无法下载')
                        continue

                    f=open(str(number)+'.jpg','wb')
                    f.write(pic.content)
                    f.close()
                else:
                    print("av" + str(number) + " 视频不存在！")

        else:
            print("av"+str(number)+" 视频不存在！")


download(number1,number2)