#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yq1ng
# @Date:   2021-03-27 14:20:49
# @Last Modified by:   yq1ng
# @Last Modified time: 2021-03-28 09:26:54

import requests

#  ------配置修改处-------
username = ''       #  云上黄淮账户（学号）
password = ''       #  云上黄淮密码
deviceId = ''       #  设备id
clientId = ''       #  客户端id
#  ------配置修改结束-------

def getToken():
    """
        获取用户idToken
    """

    # 准备数据
    url = 'https://token.huanghuai.edu.cn/password/passwordLogin'
    data = {
        'username':'',
        'password':'',
        'appId':'com.lantu.MobileCampus.huanghuai',
        'geo':'',
        'deviceId':'',
        'osType':'android',
        'clientId':''
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9'
    }

    #  设置参数
    data['username'] = username
    data['password'] = password
    data['deviceId'] = deviceId
    data['clientId'] = clientId

    #  发送数据并获取响应包
    req = requests.post(url, headers=headers, data=data)

    #  得到 idToken
    idToken = req.text[17:-1].split(':')[2].split(',')[0][1:-1]

    #  保存token
    saveidToken(idToken)

def saveidToken(idToken):
    """
        保存idToken
    """
    fp = open('/opt/healthCheck-in/cookies.txt','w')
    fp.write(idToken)
    fp.close()

if __name__=="__main__":
    getToken()
