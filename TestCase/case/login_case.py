#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/8 15:00
# @Author   : huyx
# @Site     : 
# @File     : login_case.py
# @Software : PyCharm

from TestCase.case import *


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
        self.image = Image()  ## 初始化截屏功能


    def is_element_exist(self, first, second, msg=None):
        try:
            self.assertEqual(first, second, msg=None)
        except AssertionError:
            self.image.catch_image(self.driver)
            raise

    def test_password_login_page(self):
        '''账户密码登录页面元素'''
        time.sleep(1)
        driver = self.driver
        welcome_banner = driver.find_element_by_id('com.yiche.ycysj:id/tvTitle')
        self.is_element_exist(welcome_banner.text, '欢迎登录林润云收单系统')
        account_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber')
        self.is_element_exist(account_hint_message.text, '请输入手机号')
        password_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPassword')
        self.is_element_exist(password_hint_message.text, '请输入密码')
        login_button = driver.find_element_by_id('com.yiche.ycysj:id/btnLogin')
        self.is_element_exist(login_button.text, '登录')
        forget_password = driver.find_element_by_id('com.yiche.ycysj:id/tvForgetPassword')
        self.is_element_exist(forget_password.text, '忘记密码？')
        phone_quick_login = driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin')
        self.is_element_exist(phone_quick_login.text, '手机号快捷登录')

    def test_sms_login_page(self):
        '''手机号快捷登录页面元素'''
        driver = self.driver
        driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').click()
        time.sleep(1)
        welcome_banner = driver.find_element_by_id('com.yiche.ycysj:id/tvTitle')
        self.is_element_exist(welcome_banner.text, '欢迎登录林润云收单系统')
        account_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber')
        self.is_element_exist(account_hint_message.text, '请输入手机号')
        password_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPassword')
        self.is_element_exist(password_hint_message.text, '请输入验证码')
        get_verification_code = driver.find_element_by_id('com.yiche.ycysj:id/mvSendSmsCode')
        self.is_element_exist(get_verification_code.text, '获取验证码')
        login_button = driver.find_element_by_id('com.yiche.ycysj:id/btnLogin')
        self.is_element_exist(login_button.text, '登录')
        account_password_login = driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin')
        self.is_element_exist(account_password_login.text, '账号密码登录')

    def test_error_account(self):
        '''用户名不存在'''
        driver = self.driver
        driver.find_element_by_id("com.yiche.ycysj:id/etPhoneNumber").send_keys("11503760050")  # 输入账号
        driver.find_element_by_id("com.yiche.ycysj:id/etPassword").send_keys("a123456")  # 输入密码
        driver.find_element_by_id("com.yiche.ycysj:id/btnLogin").click()  # 点击登录
        time.sleep(1)
        # error_account =

    def test_error_pwd(self):
        '''密码错误'''
        driver = self.driver
        driver.find_element_by_id("com.yiche.ycysj:id/etPhoneNumber").send_keys("11503760050")  # 输入账号
        driver.find_element_by_id("com.yiche.ycysj:id/etPassword").send_keys("a123456")  # 输入密码
        driver.find_element_by_id("com.yiche.ycysj:id/btnLogin").click()  # 点击登录
        time.sleep(1)




    def test_login(self):
        '''账户密码登录'''
        driver = self.driver
        driver.find_element_by_id("com.yiche.ycysj:id/etPhoneNumber").send_keys("15503760050")  # 输入账号
        driver.find_element_by_id("com.yiche.ycysj:id/etPassword").send_keys("a123456")  # 输入密码
        time.sleep(3)
        driver.find_element_by_id("com.yiche.ycysj:id/btnLogin").click()  # 点击登录

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
