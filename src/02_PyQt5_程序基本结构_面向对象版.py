# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 02_PyQt5_程序基本结构_面向对象版.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-22 23:57:37
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("基本程序结构面向对象版")
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        """
        设置子控件
        :return:
        """
        btn = QPushButton(self)
        # 设置内容
        btn.setText("当前按钮")
        btn.move(205, 5)    # 居中显示


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()
    window.show()

    sys.exit(app.exec_())
