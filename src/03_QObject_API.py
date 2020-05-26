# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 03_QObject_API.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-26 18:00:29
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QObject的学习")
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        """
        设置子控件
        :return:
        """
        self.get_Qobject_parent_cls()

    def get_Qobject_parent_cls(self):
        """
        QObject继承结构测试
        :return:
        """
        # QObject.__subclasses__()    # 获取QObject的子类
        mro_list = QObject.mro()
        print(mro_list)


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()
    window.show()

    sys.exit(app.exec_())
