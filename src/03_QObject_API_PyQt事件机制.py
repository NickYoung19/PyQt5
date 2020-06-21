# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 03_QObject_API_PyQt事件机制.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-06-21 23:29:39
# Copyright (C) 2020 Nick Ltd. All rights reserved.
import sys
from PyQt5.Qt import *


class App(QApplication):
    def notify(self, receiver, event):
        """
        重写notify通知方法
        :param receiver: 事件接收者
        :param event: 事件对象
        :return: 将receiver和event传递给QApplication对象的notify()方法
        """
        if receiver.inherits("QPushButton") and event.type() == QEvent.MouseButtonPress:
            # 判断只打印继承至QPushButton 且 事件类型为鼠标按下的对象
            print("事件接收者: ", receiver, "事件对象: ", event)
        return super().notify(receiver, event)  # 调用父类的notify方法并返回


class Btn(QPushButton):
    # 重写event方法
    def event(self, event):
        if event.type() == QEvent.MouseButtonPress:
            print("事件对象: ", event)
        return super().event(event)

    # 重写mousePressEvent(鼠标按下事件)
    def mousePressEvent(self, *args, **kwargs):
        print("鼠标被按下了...... from 自定义鼠标按下事件")

        # 这里如果不调用父类的pressEvent方法, 是不会调用下面的cao方法的, 因为上面重写了mousePressEvent方法
        # return super().mousePressEvent(*args, **kwargs)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    app = App(sys.argv)
    window = QWidget()

    # btn = QPushButton(window)
    btn = Btn(window)
    btn.setText("按钮")
    btn.move(100, 100)

    def cao():
        print("按钮被点击了 from cao")

    btn.pressed.connect(cao)    # 按钮按下时连接槽, 以触发槽方法

    window.show()

    sys.exit(app.exec_())
