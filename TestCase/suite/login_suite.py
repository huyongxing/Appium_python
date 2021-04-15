#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 13:05
# @Author   : huyx
# @Site     : 
# @File     : login_suite.py
# @Software : PyCharm

from TestCase.suite import *


def suite():
    suite = unittest.TestSuite()
    # suite.addTest(login_case.Login_Case('test_login'))
    suite.addTest(login_case.Login_Case('test_password_login_page'))
    suite.addTest(login_case.Login_Case('test_sms_login_page'))

    return suite
