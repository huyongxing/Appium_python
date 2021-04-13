#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 13:29
# @Author   : huyx
# @Site     :
# @File     : __init__.py
# @Software : PyCharm

from function import *


def get(title, string):
    try:
        root_path = os.path.abspath(os.path.dirname(__file__)).split('Appium_python')[0]
        path = root_path + "\\Appium_python\\function\\config"
        config = configparser.ConfigParser()
        config.read(path + "\\Config.ini")
        result = config.get(title, string)
        return result
    except Exception as e:
        logging.error("获取配置报错：" + e)


if __name__ == '__main__':
    print(get("url", "web_url"))
    print(get("account", "xs_account"))
