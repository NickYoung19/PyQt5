# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 03_QObject_定时器案例.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-06-26 23:45:25
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QObject定时器案例_倒计时")
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        """
        设置子控件
        :return:
        """
        pass


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 30px;")
        self.timer_id = self.startTimer(1000)   # 开启一个定时器

    def timerEvent(self, *args, **kwargs):
        current_sec = int(self.text())  # 取出label标签的内容
        current_sec -= 1    # 实现倒计时
        self.setText(str(current_sec))
        if current_sec == 0:
            # 结束定时器
            print("定时器已结束...")
            self.killTimer(self.timer_id)


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()

    label = MyLabel(window)
    # label.setText("10")
    # label.move(100, 100)
    # label.setStyleSheet("font-size: 30")
    # timer_id = label.startTimer(1000)

    window.show()
    sys.exit(app.exec_())

