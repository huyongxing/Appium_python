#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:52
# software: PyCharm

import os
import time
import unittest
import paramiko
from function import *
from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport

root_path = os.path.abspath(os.path.dirname(__file__)).split('Appium_python')[0]
path = root_path + "\\Appium_python\\Report\\html\\"
directory_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))


class Report():
    def upload_remote_server(file_name):
        ip = get("remote", "ip")
        port = int(get("remote", "port"))
        user = get("remote", "user")
        pwd = get("remote", "pwd")
        ssh = paramiko.Transport((ip, port))
        ssh.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(ssh)
        remote_file = "/home/wwwroot/report/" + file_name.split("\\")[-2] + "/" + file_name.split("\\")[-1]
        try:
            sftp.put(file_name, remote_file)
        except Exception as e:
            sftp.mkdir("/home/wwwroot/report/" + file_name.split("\\")[-2])
            sftp.put(file_name, remote_file)
        finally:
            return "http://report.huyx.saasyc.com/" + file_name.split("\\")[-2] + "/" + file_name.split("\\")[-1]

    def build_report(suite_tests, report_name, description):
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        report_name = report_name + picture_time
        try:
            File_Path = path + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)
        try:
            BeautifulReport(suite_tests).report(filename=report_name, description=description,
                                                report_dir=File_Path)
            return File_Path + report_name + '.html'

        except BaseException as pic_msg:
            print("生成报告失败：%s" % pic_msg)

    def report(suite_tests, report_name, description):
        try:
            name = Report.build_report(suite_tests, report_name, description)
            report_path = Report.upload_remote_server(name)
            print(report_path)

        except Exception as e:
            return False
        return True


if __name__ == '__main__':
    # Report.sent_email("C:\\Users\\Administrator\\Desktop\\new_file.html")

    local="D:\work\Appium_python\\Report\html\\2020-02-08\Report2020-02-08-11_12_34.html"
    report=Report.upload_remote_server(local)
    print(report)
