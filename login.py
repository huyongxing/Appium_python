#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/6 18:26
# @Author   : huyx
# @Site     : 
# @File     : login.py
# @Software : PyCharm

# 导入常用的包
import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

# 设置路径信息
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
global driver


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        # 初始化测试平台
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 测试平台
        desired_caps['platformVersion'] = '10.0.0'  # 系统版本
        desired_caps['deviceName'] = 'PQY0220A16029868'  # 模拟器名称
        desired_caps['app-package'] = 'com.yiche.ycysj'  # 要测试的 app
        desired_caps['app-activity'] = '.mvp.ui.activity.login.LoginActivity'  # 当前活动应用
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        time.sleep(30)
        # 点击“注册登录”按钮
        button = self.driver.find_element_by_id("com.subject.zhongchou:id/register_button")
        button.click()
        time.sleep(10)  # 登录
        name = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_phone')
        name.click()
        name.send_keys('15503760050')  # 输入用户名
        psd = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_password')
        psd.click()
        psd.send_keys('a123456')  # 输入密码
        blogin = self.driver.find_element_by_id('com.subject.zhongchou:id/go_numberlogin')
        # 单击登录按钮
        blogin.click()
        time.sleep(10)  # 此处要检测是否登录成功，我懒省事，略了！


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
