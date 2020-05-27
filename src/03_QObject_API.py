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
        self.operate_objName_property()

    def get_Qobject_parent_cls(self):
        """
        QObject继承结构测试
        :return:
        """
        # QObject.__subclasses__()    # 获取QObject的子类
        mro_list = QObject.mro()
        print(mro_list)

    def operate_objName_property(self):
        """
        QObject对象名称和属性的操作
        :return:
        """
        # 测试API
        obj = QObject()
        obj.setObjectName("notice")     # 给一个Qt对象设置一个名称, 一般这个名称是唯一的, 当做对象的ID来用
        print('obj设置的对象名称为: ', obj.objectName())   # 获取一个Qt对象的名称

        obj.setProperty("notice_level1", "error")   # 给一个Qt对象动态添加一个属性和值
        obj.setProperty("notice_level2", "warning")
        print("获取对象obj设置属性notice_level1的值为: ", obj.property("notice_level1"))   # 获取对象obj的属性值
        print("获取对象obj所有设置的属性名称: ", obj.dynamicPropertyNames())     # 获取对象obj中所有通过setProperty设置的属性名称


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()
    window.show()

    sys.exit(app.exec_())
