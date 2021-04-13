#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 13:05
# @Author   : huyx
# @Site     : 
# @File     : login_suite.py
# @Software : PyCharm

from test_case.case import *
from test_case.case import login_case

def suite():
    suite = unittest.TestSuite()
    suite.addTest(login_case.Login_Case('home_page'))

    return suite
