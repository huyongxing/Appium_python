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
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['noReset'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.image = Image()  ## 初始化截屏功能

    def element_exist(self, first, second, msg=None):
        try:
            self.assertEqual(first, second, msg=None)
        except AssertionError:
            self.image.catch_image(self.driver)
            raise

    def toast_exist(self, text, timeout=5, poll_frequency=0.01):
        driver = self.driver
        toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
        toast = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_element))
        return toast.text

    # def test_password_login_page(self):
    #     '''账户密码登录页面元素'''
    #     time.sleep(1)
    #     driver = self.driver
    #     welcome_banner = driver.find_element_by_id('com.yiche.ycysj:id/tvTitle').text
    #     self.element_exist(welcome_banner, '欢迎登录林润云收单系统')
    #     account_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').text
    #     self.element_exist(account_hint_message, '请输入手机号')
    #     password_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPassword').text
    #     self.element_exist(password_hint_message, '请输入密码')
    #     login_button = driver.find_element_by_id('com.yiche.ycysj:id/btnLogin').text
    #     self.element_exist(login_button, '登录')
    #     forget_password = driver.find_element_by_id('com.yiche.ycysj:id/tvForgetPassword').text
    #     self.element_exist(forget_password, '忘记密码？')
    #     phone_quick_login = driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').text
    #     self.element_exist(phone_quick_login, '手机号快捷登录')
    #
    # def test_error_account(self):
    #     '''用户不存在'''
    #     time.sleep(1)
    #     driver = self.driver
    #     driver.find_element_by_id("com.yiche.ycysj:id/etPhoneNumber").send_keys("11103760050")  # 输入账号
    #     driver.find_element_by_id("com.yiche.ycysj:id/etPassword").send_keys("a123456")  # 输入密码
    #     driver.find_element_by_id("com.yiche.ycysj:id/btnLogin").click()  # 点击登录
    #     self.toast_exist('用户不存在')
    #
    # def test_error_pwd(self):
    #     '''密码输入错误'''
    #     time.sleep(1)
    #     driver = self.driver
    #     driver.find_element_by_id("com.yiche.ycysj:id/etPhoneNumber").send_keys("15503760050")  # 输入账号
    #     driver.find_element_by_id("com.yiche.ycysj:id/etPassword").send_keys("a111111")  # 输入密码
    #     driver.find_element_by_id("com.yiche.ycysj:id/btnLogin").click()  # 点击登录
    #     self.toast_exist('密码输入错误')
    #
    # def test_login(self):
    #     '''账户密码登录'''
    #     time.sleep(1)
    #     driver = self.driver
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').send_keys('15503760050')  # 输入账号
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPassword').send_keys('a123456')  # 输入密码
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnLogin').click()  # 点击登录
    #     time.sleep(3)
    #     driver.find_element_by_id('com.yiche.ycysj:id/i_workspace').click()
    #
    #
    # def test_sms_login_page(self):
    #     '''手机号快捷登录页面元素'''
    #     time.sleep(1)
    #     driver = self.driver
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').click()
    #     time.sleep(1)
    #     welcome_banner = driver.find_element_by_id('com.yiche.ycysj:id/tvTitle').text
    #     self.element_exist(welcome_banner, '欢迎登录林润云收单系统')
    #     account_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').text
    #     self.element_exist(account_hint_message, '请输入手机号')
    #     password_hint_message = driver.find_element_by_id('com.yiche.ycysj:id/etPassword').text
    #     self.element_exist(password_hint_message, '请输入验证码')
    #     get_verification_code = driver.find_element_by_id('com.yiche.ycysj:id/mvSendSmsCode').text
    #     self.element_exist(get_verification_code, '获取验证码')
    #     login_button = driver.find_element_by_id('com.yiche.ycysj:id/btnLogin').text
    #     self.element_exist(login_button, '登录')
    #     account_password_login = driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').text
    #     self.element_exist(account_password_login, '账号密码登录')
    #
    # def test_phone_format(self):
    #     '''手机号格式验证'''
    #     time.sleep(2)
    #     driver = self.driver
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').click()
    #     time.sleep(1)
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').send_keys('1550376005')
    #     driver.find_element_by_id('com.yiche.ycysj:id/mvSendSmsCode').click()
    #     self.toast_exist('手机号格式不正确')
    #
    # def test_sms_code(self):
    #     '''验证码验证'''
    #     time.sleep(2)
    #     driver = self.driver
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').click()
    #     time.sleep(1)
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').send_keys('15503760050')
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPassword').send_keys('111111')
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnLogin').click()
    #     self.toast_exist('请输入正确的验证码')
    #
    # def test_getsms_success(self):
    #     '''获取短信验证码'''
    #     time.sleep(2)
    #     driver = self.driver
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').click()
    #     time.sleep(1)
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').send_keys('15503760050')
    #     driver.find_element_by_id('com.yiche.ycysj:id/mvSendSmsCode').click()
    #     self.toast_exist('获取短信验证码成功')
    #
    # def test_phone_sms_login(self):
    #     '''短信验证码登录'''
    #     time.sleep(1)
    #     driver = self.driver
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnQuickLogin').click()
    #     time.sleep(1)
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').send_keys('15503760050')
    #     driver.find_element_by_id('com.yiche.ycysj:id/mvSendSmsCode').click()
    #     time.sleep(1)
    #     driver.find_element_by_id('com.yiche.ycysj:id/etPassword').send_keys('123456')
    #     driver.find_element_by_id('com.yiche.ycysj:id/btnLogin').click()
    #     time.sleep(3)
    #     driver.find_element_by_id('com.yiche.ycysj:id/i_workspace').click()
    #
    def test_forget_pwd_page(self):
        '''忘记密码页面元素'''
        time.sleep(1)
        driver = self.driver
        driver.find_element_by_id('com.yiche.ycysj:id/tvForgetPassword').click()
        time.sleep(1)
        forgetpwd_title = driver.find_element_by_id('com.yiche.ycysj:id/toolbar_mytitle').text
        self.element_exist(forgetpwd_title, '忘记密码')
        forgetpwd_phone = driver.find_element_by_id('com.yiche.ycysj:id/etPhoneNumber').text
        self.element_exist(forgetpwd_phone, '请输入手机号')
        forgetpwd_sms = driver.find_element_by_id('com.yiche.ycysj:id/etPassword').text
        self.element_exist(forgetpwd_sms, '请输入验证码')


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
