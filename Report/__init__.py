#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:52
# software: PyCharm

import os
import time
import unittest
from BeautifulReport import BeautifulReport

class Report():
    def report(self):
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        localpath = os.getcwd()