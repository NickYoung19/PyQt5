# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : qr_code.py  v1.0
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-06-28 11:02:24
# @Description : 动态二维码生成器
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from MyQR import myqr
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("动态二维码生成工具")
        self.setWindowIcon(QIcon('C:/Users/Nick/Desktop/logo.jpg'))
        self.resize(500, 400)                           # 设置主窗口大小
        self.setFixedSize(self.width(), self.height())  # 禁止最大化按钮
        self.btn1 = QPushButton("二维码内容", self)     # 二维码内容按钮
        self.btn2 = QPushButton(self)                   # 选择背景按钮
        self.btn3 = QPushButton(self)                   # 立即生成按钮
        self.btn4 = QPushButton(self)                   # 图片路径按钮
        self.lineEdit1 = QLineEdit(self)                # 二维码内容输入框
        self.lineEdit2 = QLineEdit(self)                # 背景图片路径显示框
        self.lineEdit3 = QLineEdit(self)                # 生成图片路径显示框
        self.label = QLabel(self)                       # 二维码图片展示
        self.label1 = QLabel(self)                      # 生成状态提示
        self.pic_path = ""                              # 背景图片路径
        self.setup_ui()

    def setup_ui(self):
        """
        设置子控件UI
        :return:
        """
        self.btn1.move(20, 10)
        self.btn1.setToolTip("请在右侧条形框输入要生成二维码的内容~")

        self.btn2.setText("选择背景")
        self.btn2.setToolTip("点击选择要插入的背景图片")
        self.btn2.move(20, 40)
        self.btn2.clicked.connect(self.choose_background)

        self.btn3.setText("立\n即\n生\n成")
        self.btn3.setToolTip("点击生成二维码")
        self.btn3.move(450, 10)
        self.btn3.resize(32, 82)
        self.btn3.clicked.connect(self.generate_qr_code)

        self.btn4.setText("图片路径")
        self.btn4.move(20, 70)

        self.lineEdit1.move(100, 12)
        self.lineEdit1.setPlaceholderText("请先输入二维码内容")
        self.lineEdit1.setStyleSheet("width: 300px; color: blue;")

        self.lineEdit2.move(100, 42)
        self.lineEdit2.setStyleSheet("width: 300px;")
        self.lineEdit3.move(100, 72)
        self.lineEdit3.setStyleSheet("width: 300px;")

        self.label.move(100, 120)
        self.label.resize(260, 260)

        self.label1.move(20, 380)
        self.label1.resize(450, 20)

    def recover_style(self):
        self.lineEdit1.setStyleSheet("color: black;")

    def choose_background(self):
        """
        选择背景图片
        :return:
        """
        self.pic_path, jud = QFileDialog.getOpenFileName(self, '打开文件', './', "Image Files (*.jpg *.png *.gif)")
        self.lineEdit2.setText(self.pic_path.replace("/", "\\"))
        self.lineEdit2.setStyleSheet("color: black")

        self.label1.setText("")

    def generate_qr_code(self):
        """
        生成二维码
        :return:
        """
        try:
            # 二维码内容和背景图片都存在的情况
            if self.pic_path and self.lineEdit1.text():
                f_name = self.pic_path.split('/')[-1]
                # 限制只生成Gif的二维码
                if f_name.split('.')[1] == "gif":
                    ver, level, qr_name = myqr.run(
                        words=self.lineEdit1.text(),
                        picture=self.pic_path,
                        colorized=True,
                        save_name=f_name.split('.')[0] + "_qrcode." + f_name.split('.')[1]
                    )
                    self.lineEdit3.setText(qr_name)     # 将生成二维码图片的路径显示出来
                    qr_code = QtGui.QPixmap(qr_name)    # 打开生成的二维码图片，存放在变量png中
                    self.label.setPixmap(qr_code)       # 展示在label中

                    self.label1.setText("状态: 生成成功! ")   # 状态提示
                    self.label1.setStyleSheet("color: green")
                else:
                    self.label1.setText("状态: 生成失败, 背景图片格式错误! ")
                    self.label1.setStyleSheet("color: #e54d42")

                    self.lineEdit2.setText("请选择Gif格式的背景图片!")
                    self.lineEdit2.setStyleSheet("color: #e54d42")
            # 背景图片存在, 二维码为空的情况
            elif self.pic_path and not self.lineEdit1.text():
                self.lineEdit1.setPlaceholderText("请先输入要生成二维码的内容")
                self.lineEdit2.setStyleSheet("color: #e54d42")

                self.label1.setText("状态: 生成失败, 请先输入要生成二维码的内容! ")
                self.label1.setStyleSheet("color: #e54d42")
            # 背景图片不存在的情况
            else:
                self.lineEdit2.setText("请先选择背景图片!")
                self.lineEdit2.setStyleSheet("color: #e54d42")

                self.label1.setText("状态: 生成失败, 请根据错误提示操作! ")
                self.label1.setStyleSheet("color: #e54d42")
        except Exception as e:
            print("错误信息：%s", e)
            self.label1.setText("状态: 生成失败, 请重启软件重试! ")
            self.label1.setStyleSheet("color: #e54d42")


if __name__ == '__main__':
    import sys
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 实例化一个窗口控件
    window = Window()
    window.show()

    sys.exit(app.exec_())
