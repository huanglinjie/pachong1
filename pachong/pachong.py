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
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
response = requests.get("https://music.163.com/#/playlist?id=5028355122",headers=headers)
print(response.text)