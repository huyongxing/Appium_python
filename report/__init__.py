#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/4/13 15:38
# @Author   : huyx
# @Site     : 
# @File     : __init__.py
# @Software : PyCharm

import os
import time
import logging
from logging import handlers
from BeautifulReport import BeautifulReport
from function import *

root_path = os.path.abspath(os.path.dirname(__file__)).split('Appium_python')[0]
path = root_path + "\\Appium_python\\report\\html\\"
log_path = root_path + "\\Appium_python\\report\\logs\\"
directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
log_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))


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

    def addAttach(apath, filename='Report.html'):
        with open(apath, 'rb') as fp:
            attach = MIMEBase('application', 'octet-stream')
            attach.set_payload(fp.read())
            attach.add_header('Content-Disposition', 'attachment', filename=filename)
            encoders.encode_base64(attach)
            fp.close()
            return attach

    def report(suite_tests, report_name, description):
        try:
            name = Report.build_report(suite_tests, report_name, description)
            report_path = Report.upload_remote_server(name)
            print(report_path)
            # Report.sent_email(name)
        except Exception as e:
            return False
        return True


class Logs():
    def __init__(self):
        try:
            File_Path = root_path + '\\Appium_python\\report\\logs\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)
        self.log = Logger(File_Path + log_time + '.log', level='debug')

    def log_info(self, logs):
        self.log.logger.info(logs)

    def log_debug(self, logs):
        self.log.logger.debug(logs)

    def log_error(self, logs):
        self.log.logger.error(logs)

    def log_warning(self, logs):
        self.log.logger.warning(logs)

    def log_critical(self, logs):
        self.log.logger.critical(logs)


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        # sh = logging.StreamHandler()#往屏幕上输出
        # sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        # self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)


if __name__ == '__main__':
    # Report.sent_email("C:\\Users\\Administrator\\Desktop\\new_file.html")

    local = "C:\\Users\\huyx\\PycharmProjects\\Appium_python\\report\html\\2021-04-013\Report2021-04-13-11_12_34.html"
    report = Report.upload_remote_server(local)
    print(report)
