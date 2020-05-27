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
        # ************* 测试API *************开始
        # obj = QObject()
        # obj.setObjectName("notice")     # 给一个Qt对象设置一个名称, 一般这个名称是唯一的, 当做对象的ID来用
        # print('obj设置的对象名称为: ', obj.objectName())   # 获取一个Qt对象的名称
        #
        # obj.setProperty("notice_level1", "error")   # 给一个Qt对象动态添加一个属性和值
        # obj.setProperty("notice_level2", "warning")
        # print("获取对象obj设置属性notice_level1的值为: ", obj.property("notice_level1"))   # 获取对象obj的属性值
        # print("获取对象obj所有设置的属性名称: ", obj.dynamicPropertyNames())     # 获取对象obj中所有通过setProperty设置的属性名称
        # ************* 测试API *************结束

        # ************* 案例演示 *************开始
        label = QLabel(self)
        # 给label设置文本
        label.setText("疫情之下, 你看到的是困境")
        label.setObjectName("notice")
        # 方式一: 利用QSS样式表给label文本设置样式
        # label.setStyleSheet("font-size: 20px; color: red;")
        # 方式二: 将qss样式独立出去, 像HTML中的css一样
        with open("03_QObject_API.qss", "r") as f:
            app.setStyleSheet(f.read())

        label2 = QLabel(self)
        label2.move(100, 50)
        label2.setText("别人看到的是机遇...")
        label2.setObjectName("notice")

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.setObjectName("notice1")

        # QLabel标签, ID(对象名称)为notice, 属性值为normal的显示绿色(qss写法: QLabel#notice[notice_level="normal"])
        label3 = QLabel(self)
        label3.setText("正常的标签显示绿色")
        label3.move(100, 150)
        label3.setObjectName("notice")
        label3.setProperty("notice_level", "normal")

        # QLabel标签, ID(对象名称)为notice, 属性值为warning的显示黄色(qss写法: QLabel#notice[notice_level="warning"])
        label4 = QLabel(self)
        label4.setText("警告的标签显示黄色")
        label4.move(100, 200)
        label4.setObjectName("notice")
        label4.setProperty("notice_level", "warning")

        # QLabel标签, ID(对象名称)为notice, 属性值为error的显示红色(qss写法: QLabel#notice[notice_level="error"])
        label5 = QLabel(self)
        label5.setText("错误的标签显示红色")
        label5.move(100, 250)
        label5.setObjectName("notice")
        label5.setProperty("notice_level", "error")
        # ************* 案例演示 *************结束


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()
    window.show()

    sys.exit(app.exec_())
