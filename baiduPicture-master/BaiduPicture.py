import re,requests,json,threading
import common

# rn表示图片个数，最大60张
# pn表示从第几张图片开始
# word表示关键字
# 必填字段tn=resultjson_com，ipn=rj，确保编码字段ie,oe虽然编码不影响，以防万一还是用上
# https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ie=utf-8&oe=utf-8&word=炮姐&pn=0&rn=2
# 从第0张图片开始，返回包含2张（即0与1的图片）数据的json 注：实际返回的json中data列表中包含3个，最后一个为空，前两个为第0与1图片的对象


# 获取一页60张图片url组成的list
def getBaiduUrlList(text):
    # jsonobj = json.loads(text)
    # data = jsonobj['data']
    # # 获取所有图片的url，组成list
    # pictureList = []
    # for i in range(0,len(data)-1):
    #      # print(i)
    #      data0 = data[i]
    #      pictureList.append(data0['thumbURL'])
    # print(pictureList)

    # 因为pn=0时返回的json有错误所以用正则表达式来提取所有url组成list
    pattern = re.compile(r'"thumbURL":"(.*?)","middleURL"',re.S)
    pictureList = re.findall(pattern,text)
    # print(pictureList)
    return pictureList

#     下载百度图片
def downloadBiduPicture(keyword,startpage,endpage):
    # 创建文件夹
    common.makedir(str(keyword))
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'}
    # 控制页数的循环
    while (int(startpage) < int(endpage)):
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ie=utf-8&oe=utf-8&word='+str(keyword)+'&pn='+str(startpage)+'&rn=60'
        text = requests.get(url=url,headers=headers).text
        # print(text)
        pictureList = getBaiduUrlList(text)
        for count in range(0,len(pictureList)):
            try:
                name = str(keyword)+'_'+str(startpage)+'_'+str(count)
                type = '.jpg'
                # 多线程下载
                mythread = threading.Thread(target=common.downloadPicture, args=(pictureList[count], name, type))
                mythread.start()
                # 控制线程数目为64
                if (threading.activeCount()>=64):
                    mythread.join()
                print('thread name:' + str(mythread.name))
                print(str(threading.activeCount()) + 'actived thread')
            except:
                print(print('当前（第' + str(count) + '）图片下载超时，正在下载下一张'))
        # 控制循环
        startpage +=1

if __name__== '__main__':
    downloadBiduPicture('炮姐',0,3)
    common.pringThreadNumberEverySecond()
