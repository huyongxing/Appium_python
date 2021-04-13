#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 13:29
# @Author   : huyx
# @Site     : 
# @File     : __init__.py
# @Software : PyCharm

import os,math

if __name__ == '__main__':
    try:
        cmd = 'taskkill /F /IM chromedriver.exe'
        os.system(cmd)


    except Exception as e:
        print(e)
