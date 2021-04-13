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
from HTMLTestRunner import HTMLTestRunner

test_dir = './case'
discover = unittest.defaultTestLoader.discover(start_dir='./case', pattern="ycysj*.py")

# if __name__ == "__main__":
    # # 实例化测试套件
    # suite = unittest.TestSuite()
    # # 加载测试用例
    # suite.addTest(LoginTest('test_login'))
    # # 生成测试报告
    # # 选择指定时间格式
    # timestr = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
    # # 定义测试报告存放路径和报告名称
    # filename = 'D:\\report.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='自动化测试报告', description='执行人：胡永行')
    # runner.run(suite)  # 关闭测试报告
    # fp.close()
if __name__ == "__main__":
    report_dir = './report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="自动化测试报告", description="APP自动化测试报告")
        runner.run(discover)