#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 13:14
# @Author   : huyx
# @Site     : 
# @File     : __init__.py
# @Software : PyCharm

import time
import math
import unittest
import HTMLTestRunner
from appium import webdriver
from Report import *
from TestCase.data import *
from function import *
from function.element import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By