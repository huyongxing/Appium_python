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


class Login_Case(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0.0'
        desired_caps['deviceName'] = 'PQY0220A16029868'
        desired_caps['appPackage'] = 'com.yiche.ycysj'
        desired_caps['appActivity'] = 'com.newpro.activity.start.LoadingActivity'
        desired_caps['appWaitActivity'] = 'com.yiche.ycysj.mvp.ui.activity.login.LoginActivity'
        desired_caps['appWaitDuration'] = '50000'
        desired_caps['noReset'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def is_element_exist(self, mode, located):
        global flag
        try:
            if mode == 'id':
                self.driver.find_elements_by_id(located)
            elif mode == 'xpath':
                self.driver.find_elements_by_xpath(located)
            elif mode == 'class':
                self.driver.find_elements_by_class_name(located)
            elif mode == 'css':
                self.driver.find_elements_by_css_selector(located)
            else:
                self.driver.find_elements(mode, located)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag

    def home_page(self):
        welcome_banner = self.driver.find_elements_by_id('com.yiche.ycysj:id/tvTitle')
        self.is_element_exist(welcome_banner.text, '欢迎登录林润云收单系统')
        account_hint_message = self.driver.find_elements_by_id('com.yiche.ycysj:id/etPhoneNumber')
        self.is_element_exist(account_hint_message.text, '请输入手机号')
        password_hint_message = self.driver.find_elements_by_id('com.yiche.ycysj:id/etPassword')
        self.is_element_exist(password_hint_message.text, '请输入密码')
        login_button = self.driver.find_elements_by_id('com.yiche.ycysj:id/btnLogin')
        self.is_element_exist(login_button.text, '登录')
        forget_password = self.driver.find_elements_by_id('com.yiche.ycysj:id/tvForgetPassword')
        self.is_element_exist(forget_password.text, '忘记密码？')
        phone_quick_login = self.driver.find_elements_by_id('com.yiche.ycysj:id/btnQuickLogin')
        self.is_element_exist(phone_quick_login.text, '手机号快捷登录')

    # def test_login(self):
    #     driver = self.driver
    #     driver.find_element_by_id("com.yiche.ycysj:id/etPhoneNumber").send_keys("15503760050")  # 输入账号
    #     driver.find_element_by_id("com.yiche.ycysj:id/etPassword").send_keys("a123456")  # 输入密码
    #     time.sleep(3)
    #     driver.find_element_by_id("com.yiche.ycysj:id/btnLogin").click()  # 点击登录
    #     time.sleep(3)


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":  # 定义一个测试容器
    print("----------执行---------- ")
    suite = unittest.TestSuite()  # 将测试用例，加入到测试容器中
    suite.addTest(Login_Case('home_page'))  # 定义个报告存放的路径，支持相对路径
    file_path = "C:\\Users\\huyx\\PycharmProjects\\Appium_python\\report\\html\\report.html"
    file_result = open(file_path, 'wb')  # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"自动化测试报告", description=u"用例执行情况")  # 运行测试用例
    runner.run(suite)
    file_result.close()

