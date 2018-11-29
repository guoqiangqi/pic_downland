import BaiduPicture,common
print("说明：\n下载页数区间为【开始页，结束页），每页60张图片\n如果想从第一页开始下载，起始页输入0\n由于服务器限制，单次下载最多下载3页（180张）")
keyword = input('输入查询关键字：')
startpage = input("输入开始起始页：")
endpage = input("输入结束页：")
# 开始下载
BaiduPicture.downloadBiduPicture(str(keyword),int(startpage),int(endpage))
# 每秒打印线程数
common.pringThreadNumberEverySecond()