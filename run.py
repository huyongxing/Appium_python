#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/12 17:41
# @Author   : huyx
# @Site     : 
# @File     : run.py
# @Software : PyCharm

import os
import time
import unittest
from appium import webdriver
import HTMLTestRunner
from BeautifulReport import BeautifulReport
from TestCase.suite import login_suite




if __name__ == "__main__":  # 定义一个测试容器
    print("----------执行---------- ")
    suite = unittest.TestSuite()  # 将测试用例，加入到测试容器中
    suite.addTest(Login_Case('home_page'))  # 定义个报告存放的路径，支持相对路径
    file_path = "C:\\Users\\huyx\\PycharmProjects\\Appium_python\\report\\html\\report.html"
    file_result = open(file_path, 'wb')  # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"自动化测试报告", description=u"用例执行情况")  # 运行测试用例
    runner.run(suite)
    file_result.close()

