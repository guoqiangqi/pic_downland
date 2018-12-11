# -*- coding: utf-8 -*-
"""
Spyder Editor ljQian

This is a apyder-Baidu-Image file.
"""
import requests
import re
from urllib import parse
from threading import Thread
import os

def download(i, j, key, url):
    header = {'content-type': 'application/json',
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
              "Connection": "keep-alive",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "Accept-Language": "zh-CN,zh;q=0.8"
              }
    response = requests.get(url, headers=header)

    link = re.findall(r'"objURL":"(.*?)"', response.text, re.S)
    if not os.path.exists(key):
        os.mkdir("./" + key + "/")

    for web in link:
        url = decodeurl(web)
        print(url)

        try:
            # allow_redirects=False 关闭重定向
            pic = requests.get(url, timeout=10, headers=header, allow_redirects=False)
            dirfile = "./" + key + "/" + key + '_' + str(j) + '.jpg'
            fp = open(dirfile, 'wb')
            fp.write(pic.content)
            fp.close()
            j += 1
        except requests.exceptions.ConnectionError:
            print(web, "【错误】当前图片无法下载")
            continue
        except requests.exceptions.ReadTimeout:
            print(web, "【错误】超时")
            continue
        except requests.exceptions.ChunkedEncodingError:
            print(web, "【错误】远程主机强迫关闭了一个现有的连接")
            continue


def decodeurl(url):
    str_table = {
        '_z2C$q': ':',
        '_z&e3B': '.',
        'AzdH3F': '/'
    }
    char_table = {
        'w': 'a',
        'k': 'b',
        'v': 'c',
        '1': 'd',
        'j': 'e',
        'u': 'f',
        '2': 'g',
        'i': 'h',
        't': 'i',
        '3': 'j',
        'h': 'k',
        's': 'l',
        '4': 'm',
        'g': 'n',
        '5': 'o',
        'r': 'p',
        'q': 'q',
        '6': 'r',
        'f': 's',
        'p': 't',
        '7': 'u',
        'e': 'v',
        'o': 'w',
        '8': '1',
        'd': '2',
        'n': '3',
        '9': '4',
        'c': '5',
        'm': '6',
        '0': '7',
        'b': '8',
        'l': '9',
        'a': '0'
    }
    char_table = {ord(key): ord(value) for key, value in char_table.items()}
    for key, value in str_table.items():
        url = url.replace(key, value)
    url = url.translate(char_table)
    return url


def main():
    j = 0
    keys = ["海豚"]
    for key in keys:
        data = parse.quote(str(key))

        for i in range(j, 2000, 30):
            if j == 0:
                j += 1
            url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&word=" + data + "&z=&ic=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&step_word=" + data + "&pn=" + str(
                i) + "&rn=30&gsm=3c&1527055161957="
            download(i, j, key, url)
            j += 30


if __name__ == "__main__":
    main()