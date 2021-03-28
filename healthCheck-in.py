#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yq1ng
# @Date:   2021-03-27 15:04:12
# @Last Modified by:   yq1ng
# @Last Modified time: 2021-03-28 09:26:49

import requests
import base64
import os

#  ------配置修改处-------
phoneNumber = ''            #  自己手机号
emergencyContactName = ''   #  紧急联系人姓名
emergencyContactPhone = ''  #  紧急联系人电话
student_number = ''         #  自己学号
#  ------配置修改结束-------


def ProcessingParameters():
    """
        处理各种健康打卡函数所需参数
    """

    #  get Referer
    fp = open('/opt/healthCheck-in/Location.txt', 'r')
    Referer = fp.read()
    fp.close()

    #  get xAuthToken
    xAuthToken = Referer.split('=')[-1]
    
    #  get Session
    Session = base64.b64encode(xAuthToken.encode()).decode()

    #  get isToken
    fp = open('/opt/healthCheck-in/cookies.txt', 'r')
    idToken = fp.read()
    fp.close()

    healthCheckIn(xAuthToken, Referer, Session, idToken)


def healthCheckIn(xAuthToken, Referer, Session, userToken):
    """
        健康打卡
    """

    #  准备数据
    url = 'https://yq.huanghuai.edu.cn:7992/questionAndAnser/wenjuanSubmit'
    data = {
        'recordId':'',
        'zuobiao':'33.011447,114.00818',
        'questionnaire':'[{"problem_id":1,"problem_name":"今日体温","result_id":null,"result_name":"36.0"},{"problem_id":2,"problem_name":"你当前的身体状况是?","result_id":2,"result_name":"正常，没有症状"}]',
        'record':'{"current_area":"河南省 驻马店市 驿城区","current_address":"黄淮学院"}',
        'phoneNumber':'',
        'emergencyContactName':'',
        'emergencyContactPhone':'',
        'student_number':''
    }
    headers = {
        'Accep':'application/json, text/plain, */*',
        'x-auth-token':'',
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 SuperApp',
        'Origin':'https://yk.huanghuai.edu.cn:8993',
        'Referer':'',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'X-Requested-With':'com.lantu.MobileCampus.huanghuai'
    }
    cookies = {
        'userToken':'',
        'Domain':'.huanghuai.edu.cn',
        'Path':'/',
        'SESSION':''
    }

    #  设置参数
    headers['phoneNumber'] = phoneNumber
    headers['emergencyContactName'] = emergencyContactName
    headers['emergencyContactPhone'] = emergencyContactPhone
    headers['student_number'] = student_number
    headers['x-auth-token'] = xAuthToken
    headers['Referer'] = Referer
    cookies['userToken'] = userToken
    cookies['SESSION'] = Session
    
    #  发送打卡数据
    req = requests.post(url, headers=headers, cookies=cookies, data=data)
    if "20000" in req.text:
        os.system('echo "今日打卡成功啦!     --会下雪的晴天" | mail -v -s "健康打卡" 1578422748\@qq.com')

def main():
    ProcessingParameters()

if __name__ == '__main__':
    main()
