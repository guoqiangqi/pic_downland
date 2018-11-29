
import requests,os,re,threading,time,json
import common

# https://chartsapi.gdgdocs.org/search?tbm=isch&q=炮姐&ijn=0
# ijn表示第几页，每页100张
# q表示关键字
# 必填项tbm=isch

# def getGooglePictureList(text):






def downloadGooglePicture(keyword,startpage,endpage):
    common.makedir(str(keyword))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
    for startpage in range(int(startpage),int(endpage)):
        url = 'https://chartsapi.gdgdocs.org/search?tbm=isch&q='+str(keyword)+'&ijn='+str(startpage)
        # print(url)
        text =requests.get(url=url,headers=headers).content
        #解码 将二进制数据转换为str
        text = text.decode()
        # print(text)
        # json解析错误，所以用正则匹配出所有图片地址
        pattern = re.compile(r',"ou":"(.*?)","ow"',re.S)
        pictureList = re.findall(pattern,text)
        # print(pictureList)
        for count in range(0,len(pictureList)):
            # 消除url编码问题：将=编码为\\u003d
            pictureList[count] = common.urlCode(pictureList[count])
            # print(pictureList[count])
            name = str(keyword)+'_'+str(startpage)+"_"+str(count)
            type = '.jpg'
            try:
                # 启动线程
                mythread = threading.Thread(target=common.downloadPicture,args=(pictureList[count],name,type))
                mythread.start()
                # 控制线程数目
                if (threading.activeCount() >= 64):
                    mythread.join()
                # 打印线程名 和线程数目
                print('thread name:'+str(mythread.name))
                print(str(threading.activeCount())+'actived thread')
            except:
                print('线程创建失败')
        startpage +=1


if __name__ == '__main__':
    downloadGooglePicture('索隆',0,2)
    # common.pringThreadNumberEverySecond()
    # 浏览器头
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
    # response = requests.get("http://httpbin.org/get",verify = False,headers = headers)
    # print(type(response.text))
    # print(response.json())
    # print(json.loads(response.text))
    # print(type(response.json()))