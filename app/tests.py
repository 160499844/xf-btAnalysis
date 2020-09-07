from django.test import TestCase
import requests
import os

import shutil

base_path = "D:/迅雷下载" #种子搜索目录
to_path = "D:/临时文件/" #种子临时存放目录
fail_path = "D:/临时文件/处理失败/" #处理失败存放

def testSearchTorrentFile():
    """全盘搜索种子文件"""
    base = os.walk(base_path)
    filesList = findAllFile(base)
    for item in filesList:
        #遍历每个种子文件
        #print(item)
        #组装信息
        try:

            info = getInfo(item)
            msg = info['msg']
            if "ok" == msg:
                data_created_by_ = info['data']['created_by']
                data_creation_date_ = info['data']['creation_date']
                data_files_ = info['data']['files']
                data_name_ = info['data']['name']
                data_length_ = info['data']['length']
                print(data_creation_date_)
                print(data_name_)
                print(item)
                print(data_length_)
                print(data_files_)
                print("---------------------------------------------------------")

                #移动到指定目录
                shutil.move(item, to_path + data_name_ + '.torrent')
            else:
                #无法获取信息
                # 移动到指定目录
                item_name = str(item).split("\\")[-1]
                shutil.move(item, fail_path + item_name)
        except Exception as e:

            print(e)
            # 移动到指定目录
            item_name = str(item).split("\\")[-1]
            shutil.move(item, fail_path + item_name)


def findAllFile(base):
    """获取种子文件"""
    list = []
    for path, d, filelist in base:

        for filename in filelist:
            filenameEnd = os.path.splitext(filename)[-1]
            if(filenameEnd=='.torrent'):
                #print(os.path.join(path, filename))
                list.append(os.path.join(path, filename))

    return list

def getInfo(filePath):
    """解析种子获取信息"""
    url = "https://api.toolnb.com/Tools/Api/btAnalysis.html"
    headers = {
        "origin":"https://www.toolnb.com",
        "referer":"https://www.toolnb.com/tools/torrentAnalysis.html",
    }
    files = {"file":open(filePath, "rb")}
    js = requests.post(url=url,headers=headers,files=files,data=None).json()
    return js
