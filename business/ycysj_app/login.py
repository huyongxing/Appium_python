#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 13:07
# @Author   : huyx
# @Site     : 
# @File     : login.py
# @Software : PyCharm

from business.ycysj_app import *

if __name__ == '__main__':
    suite_tests = login_suite.suite()
    report_name = "自动化测试报告"
    description = "登录验证"
    result = Report.report(suite_tests, report_name, description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")
