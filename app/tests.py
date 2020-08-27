from django.test import TestCase
import requests
import os

def findAllFile(base):
    list = []
    for path, d, filelist in base:

        for filename in filelist:
            filenameEnd = os.path.splitext(filename)[-1]
            if(filenameEnd=='.torrent'):
                print(os.path.join(path, filename))
                list.append(os.path.join(path, filename))
        # Create your tests here.
def testSearchTorrentFile():
    """全盘搜索种子文件"""
    base = os.walk("D:/")
    filesList = findAllFile(base)


def testGetInfo():
    """解析种子获取信息"""
    url = "https://api.toolnb.com/Tools/Api/btAnalysis.html"
    headers = {
        "origin":"https://www.toolnb.com",
        "referer":"https://www.toolnb.com/tools/torrentAnalysis.html",
    }
    files = {"file":open("D:/迅雷下载/25F406F0C39CBDBE0936DC14E415C6AF45FDD793.torrent", "rb")}
    js = requests.post(url=url,headers=headers,files=files,data=None).json()
    print(js)
