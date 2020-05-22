# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : 02_PyQt5_程序基本结构_分析.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-22 18:09:33
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)    # sys.argv: 用来接收命令行执行程序时传的参数
# print(app.arguments())        # app为当前局部的app, arguments(): 用来获取执行程序时传的参数, 返回一个列表
# print(qApp.arguments())       # qApp为全局的app

# 2. 控件的操作
# 创建控件, 设置控件(大小, 位置, 样式...), 事件, 信号的处理
# 2.1 创建控件
# 当我们创建一个控件之后, 如果说, 这个控件没有父控件, 则把它当做顶层控件(窗口)
# 系统会自动的给窗口添加一些装饰(标题栏), 窗口控件具备一些特性(设置标题, 图标)
window = QWidget()
# window = QPushButton()    # 按钮控件
# 2.2 设置控件
window.setWindowTitle("程序基本结构分析")
window.resize(400, 400)

# 控件也可以作为一个容器(承载其他的控件)
label = QLabel(window)
label.setText("标签的文字")
label.setWindowTitle("标签的标题")   # 当已指定父控件时, 此命令是无效的
label.move(100, 50)
# label.show()      # 如果没哟指定父控件的情况下, 需要用show()来显示

# 2.3 展示控件
# 刚创建好一个控件之后,(这个控件没有什么父控件), 默认情况下不会被展示,只有手动的调用show()才可以
# 如果说这个控件, 有父控件的,那么一般情况下, 父控件展示之后, 子控件会自动展示
window.show()

# 3. 应用程序的执行, 进入到消息循环
# 让整个程序开始执行,并且进入到消息循环(无限循环)
# 检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())


# sys.argv验证:
# 我们的代码, 到时候的执行方式: 1, 右击执行   2, 命令行 python 代码名称 参数[可选]
# 当别人通过命令行启动这个程序的时候,可以设定一种功能(接收命令行传递的参数, 来执行不同的业务逻辑
# sys.argv返回的是一个列表, 第一个元素是py文件名, 后面的才是传的参数
# args = sys.argv
# print(args)
# if args[1] == '1':
#     print("xxx")
# else:
#     print("ooo")

# sys.exit()
