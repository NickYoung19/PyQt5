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
        # self.get_Qobject_parent_cls()
        # self.operate_objName_property()
        # self.operate_objParent_sub()
        # self.operate_object_signal()
        self.judge_object_type()

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

    def operate_objParent_sub(self):
        """
        QObject对象的父子关系操作
        :return:
        """
        # ************* 测试API *************开始
        # obj1 = QObject()
        # obj2 = QObject()
        # print("obj1: ", obj1)
        # print("obj2: ", obj2)
        #
        # obj1.setParent(obj2)    # 将obj2设置为obj1的父对象
        # print("obj1的父对象为: ", obj1.parent())    # 获取obj1的父对象
        """
        设置如图的继承关系:
             obj0
         |-----|-----|
        obj1        obj2
         |        |---|---|
        obj3     obj4    obj5
        """
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        print("obj0: ", obj0)
        print("obj1: ", obj1)
        print("obj2: ", obj2)
        print("obj3: ", obj3)
        print("obj4: ", obj4)
        print("obj5: ", obj5)

        obj1.setParent(obj0)
        obj2.setParent(obj0)

        obj3.setParent(obj1)
        obj3.setObjectName("3")

        obj4.setParent(obj2)
        obj5.setParent(obj2)

        print("obj4的父对象: ", obj4.parent())    # parent()获取obj4的父对象, 父对象有且只有一个, 以最后设置的为准
        print("obj0的子对象: ", obj0.children())  # children()获取obj0的所有直接[一级]子对象(这里没有间接子对象, 即obj3,obj4...)

        print("obj0的第一个子对象: ", obj0.findChild(QObject))  # 获取obj0的第一个基于QObject类型的子对象
        # 要想获取间接[二级]子对象, 方法如下
        print("递归查找1: ", obj0.findChild(QObject, "3")) # 获取obj0指定对象名称的子对象(先设置对象名称为3, 再通过对象名称查找), 默认递归查找
        print("递归查找2: ", obj0.findChild(QObject, "3", Qt.FindChildrenRecursively)) # 同上, 递归查找

        print("直接子对象: ", obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly)) # 查找直接[一级]子对象, 找不到返回None

        print(obj0.findChildren(QObject))   # 查找obj0的所有基于QObject类型的子对象, 包括直接和间接子对象
        # ************* 测试API *************结束

        # ************* 内存管理机制 *************开始
        obj6 = QObject()
        self.obj6 = obj6    # 给obj6对象添加一个引用, 不让其释放(便于下面演示手动释放)

        obj7 = QObject()
        obj7.setParent(obj6)
        # 监听对象obj7是否被释放
        obj7.destroyed.connect(lambda : print("对象obj7被释放了..."))
        del self.obj6   # 删除父对象obj6, 观察子对象obj7是否也被释放
        # ************* 内存管理机制 *************结束

    def operate_object_signal(self):
        """
        QObject信号与槽的操作
        :return:
        """
        """
        self.obj7 = QObject()
        # def destroy_cao(obj):
        #     print("对象被释放了...", obj)
        #
        # self.obj7.destroyed.connect(destroy_cao)    # 连接曹
        # del self.obj7   # 手动释放对象

        def obj_name_cao(obj):
            # obj用于接收objectNameChanged信号触发传来的对象
            print("对象名称发生了改变...", obj)

        self.obj7.objectNameChanged.connect(obj_name_cao)
        self.obj7.setObjectName("XXX")  # 设置对象的名称

        # self.obj7.objectNameChanged.disconnect(obj_name_cao)    # 取消与槽的连接
        self.obj7.blockSignals(True)    # 方法二: 临时取消与槽的连接
        self.obj7.setObjectName("OOO")
        self.obj7.blockSignals(False)   # 恢复与槽的连接
        self.obj7.setObjectName("XXXOOO")

        print(self.obj7.receivers(self.obj7.objectNameChanged)) # receivers当前已连接槽的数量
        """
        # ************* 信号与槽操作案例一 *************开始
        # btn = QPushButton(self)
        # btn.setText("点我啊")
        #
        # def cao():
        #     print("点我干嘛~")
        #
        # btn.clicked.connect(cao)
        # ************* 信号与槽操作案例一 *************结束

        # ************* 信号与槽操作案例二 *************开始
        def cao(title):
            print("窗口标题发生了变化", title)
            self.blockSignals(True)     # 临时断开与槽的连接
            self.setWindowTitle("撩课 - " + title)
            self.blockSignals(False)    # 在重新设置标题后, 恢复与槽的连接

        self.windowTitleChanged.connect(cao)    # 连接信号与槽

        self.setWindowTitle("Hello Nick")   # 第一次设置标题
        self.setWindowTitle("Hello Nick2")  # 第二次设置标题
        # ************* 信号与槽操作案例二 *************结束

    def judge_object_type(self):
        """
        QObject类型的判定
        :return:
        """
        # ************* 类型的判定API *************开始
        # obj = QObject()
        # w = QWidget()
        # btn = QPushButton()
        # label = QLabel()
        # obj_li = [obj, w, btn, label]
        # for o in obj_li:
        #     # print("是否是控件类型: ", o.isWidgetType())     # isWidgetType判断是否是控件类型
        #     """
        #     是否是控件类型:  False
        #     是否是控件类型:  True
        #     是否是控件类型:  True
        #     是否是控件类型:  True
        #     """
        #     # print("是否继承父类QWidget: ", o.inherits("QWidget"))     # inherits判断对象是否(直接或间接)继承某个父类
        #     """
        #     是否继承父类QWidget:  False
        #     是否继承父类QWidget:  True
        #     是否继承父类QWidget:  True
        #     是否继承父类QWidget:  True
        #     """
        #     print("是否继承父类QPushButton: ", o.inherits("QPushButton"))     # 判断对象是否(直接或间接)继承某个父类
        #     """
        #     是否继承父类QPushButton:  False
        #     是否继承父类QPushButton:  False
        #     是否继承父类QPushButton:  True
        #     是否继承父类QPushButton:  False
        #     """
        # ************* 类型的判定API *************结束

        # ************* 类型的判定案例 *************开始
        label1 = QLabel(self)
        label1.setText("社会我顺哥")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("人狠话不多")
        label2.move(100, 150)

        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(100, 200)

        # 方法一: 给label空间设置背景颜色
        # for widget in self.findChildren(QLabel):
        #     widget.setStyleSheet("background-color: cyan;")
        # 方法二:
        for widget in self.children():
            if widget.inherits("QLabel"):
                widget.setStyleSheet("background-color: cyan;")
        # ************* 类型的判定案例 *************结束


def QWidget_parent_sub_relation():
    """
    QWidget控件的父子关系
    :return:
    """
    # win1 = QWidget()
    # win1.setWindowTitle("红色")
    # win1.resize(500, 500)
    # win1.setStyleSheet("background-color: red;")
    # win1.show()
    #
    # win2 = QWidget()
    # win2.setWindowTitle("绿色")
    # win2.setStyleSheet("background-color: green;")
    # # win2.setParent(win1)
    # win2.resize(1000, 100)
    # win2.show()

    win_root = QWidget()

    label1 = QLabel()
    label1.setText("label1")
    label1.setParent(win_root)

    label2 = QLabel()
    label2.move(50, 50)
    label2.setText("label2")
    label2.setParent(win_root)

    label3 = QLabel()
    label3.move(80, 80)
    label3.setText("label3")
    label3.setParent(win_root)

    btn = QPushButton(win_root)
    btn.move(100, 100)
    btn.setText("btn")

    win_root.show()

    for sub_widget in win_root.findChildren(QLabel):
        print(sub_widget)
        sub_widget.setStyleSheet("background-color: cyan;")


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # QWidget_parent_sub_relation()

    # 实例化一个窗口控件
    window = Window()
    window.show()

    sys.exit(app.exec_())
