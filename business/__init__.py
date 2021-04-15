#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/15 13:07
# @Author   : huyx
# @Site     : 
# @File     : __init__.py.py
# @Software : PyCharm

import os, math

if __name__ == '__main__':
    try:
        cmd = 'taskkill /F /IM Appium.exe'
        os.system(cmd)


    except Exception as e:
        print(e)
