#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yq1ng
# @Date:   2021-03-27 15:42:09
# @Last Modified by:   yq1ng
# @Last Modified time: 2021-03-28 09:26:36

import requests

def readCookies():
    """
        从本地读取cookie
    """

    #  打开文件
    fp = open('/opt/healthCheck-in/cookies.txt', 'r')
    idToken = fp.read()
    getSession(idToken)
        

def getSession(idToken):
    """
        获取用户唯一token页面
    """

    #  准备各种数据
    url = 'https://yq.huanghuai.edu.cn:7992/cas/studentLogin'
    headers = {
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 SuperApp',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'x-id-token':'',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'X-Requested-With':'com.lantu.MobileCampus.huanghuai'
    }
    cookies = {
        'userToken':'',
        'Domain':'.huanghuai.edu.cn',
        'Path':'/'
    }

    #  设置参数
    headers['x-id-token'] = idToken
    cookies['userToken'] = idToken

    #  获取session, 并禁止302
    req = requests.get(url, headers=headers, cookies=cookies, allow_redirects=False)
    saveSession(req.headers['Location'])

def saveSession(Location):
    """
        保存session
    """

    try:
        fp = open('/opt/healthCheck-in/Location.txt', 'w')
        fp.write(Location)
        fp.close()
    except Exception as e:
        exit(1)

def main():
    readCookies()

if __name__ == '__main__':
    main()
