# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 03_QObject_定时器.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-06-26 23:18:30
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QObject定时器的使用")
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        """
        设置子控件
        :return:
        """
        pass


class MyObject(QObject):
    # 自定义Object类, 重写timerEvent方法
    def timerEvent(self, QTimerEvent):
        print("1秒: ", QTimerEvent)


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()
    window.show()

    obj = MyObject()
    timer_id = obj.startTimer(1000)    # 开启一个定时器, 每1秒调一次timerEvent

    # 删除定时器
    # obj.killTimer(timer_id)

    sys.exit(app.exec_())
