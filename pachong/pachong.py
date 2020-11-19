#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 01:02
# @Author  : 黄林杰
# @File    : pachong.py
# @Software: PyCharm

import os
import requests
from bs4 import BeautifulSoup
import urllib.request
#声明一个请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
# response = requests.get("https://music.163.com/#/playlist?id=5028355122",headers=headers)
#输入的url
play_url = input("请输入你想要爬取的歌单地址：")
#保持会话
s = requests.session()
#声明响应变量
response = s.get(play_url,headers=headers).content
#实例化网页选择器
soup = BeautifulSoup(response,'lxml')
main = soup.find('ul',{'class':'f-hide'})
print(main)
