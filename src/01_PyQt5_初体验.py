# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 01_PyQt5_初体验.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-22 17:49:33
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

# 初始化一个应用对象
app = QApplication(sys.argv)

# 定义一个窗口
window = QWidget()
# 给这个窗口设置标题
window.setWindowTitle("我的第一个GUI应用")
# 设置窗口大小
window.resize(500, 400)
# 设置窗口打开出现的位置
window.move(400, 200)

# 定义一个标签, 指定主窗口为父控件
lable = QLabel(window)
# 给标签设置文本内容
lable.setText("Hello PyQt5!")
# 设置标签的位置
lable.move(215, 190)

# 显示窗口
window.show()

# 进入应用消息主循环
sys.exit(app.exec_())
