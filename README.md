# 黄淮学院健康打卡
### 简略教程

##### install

`cd /opt`  

 `git clone https://github.com/yq1ng/healthCheck-in.git`  

`pip3 install requests`  

##### 所需环境

python3.x  

requests模块

##### 配置&运行

依次按照注释提示修改三个文件，设备id去[这里](https://www.345tool.com/zh-hans/generator/random-id-generator)生成，`deviceId`24位(没有短横线)，`clientId`32位，推荐去最下面的博客看  

再运行前两个文件

```
/usr/local/bin/python3 /opt/healthCheck-in/getToken.py
/usr/local/bin/python3 /opt/healthCheck-in/getSession.py
```

此时你会拥有五个文件：`cookies.txt  getSession.py  getToken.py  healthCheck-in.py  Location.txt`

##### 定时任务

centos7：`touch /tmp/healthCheck-in.log`，`crontab -u root -e`

```
30 7 1,20 * *  /usr/local/bin/python3 /opt/healthCheck-in/getToken.py
50 7 * * *  /usr/local/bin/python3 /opt/healthCheck-in/getSession.py
00 8 * * *  /usr/local/bin/python3 /opt/healthCheck-in/healthCheck-in.py>/tmp/healthCheck-in.log 2>&1&
```



更详细的教程与抓包分析在这：https://yq1ng.github.io/z_post/%E8%87%AA%E5%8A%A8%E5%8C%96%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1/   
网不好的同学可以看csdn：https://blog.csdn.net/weixin_43578492/article/details/115276560   
祝好运~