# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 530)
        MainWindow.setMinimumSize(QtCore.QSize(720, 530))
        MainWindow.setMaximumSize(QtCore.QSize(720, 530))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 211))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 161, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 0, 4, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_parity = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_parity.sizePolicy().hasHeightForWidth())
        self.comboBox_parity.setSizePolicy(sizePolicy)
        self.comboBox_parity.setObjectName("comboBox_parity")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.gridLayout.addWidget(self.comboBox_parity, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_stop_bits = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_stop_bits.sizePolicy().hasHeightForWidth())
        self.comboBox_stop_bits.setSizePolicy(sizePolicy)
        self.comboBox_stop_bits.setObjectName("comboBox_stop_bits")
        self.comboBox_stop_bits.addItem("")
        self.comboBox_stop_bits.addItem("")
        self.comboBox_stop_bits.addItem("")
        self.gridLayout.addWidget(self.comboBox_stop_bits, 4, 1, 1, 1)
        self.comboBox_baud_rate = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_baud_rate.sizePolicy().hasHeightForWidth())
        self.comboBox_baud_rate.setSizePolicy(sizePolicy)
        self.comboBox_baud_rate.setObjectName("comboBox_baud_rate")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.comboBox_baud_rate.addItem("")
        self.gridLayout.addWidget(self.comboBox_baud_rate, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_data_bits = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_data_bits.sizePolicy().hasHeightForWidth())
        self.comboBox_data_bits.setSizePolicy(sizePolicy)
        self.comboBox_data_bits.setObjectName("comboBox_data_bits")
        self.comboBox_data_bits.addItem("")
        self.comboBox_data_bits.addItem("")
        self.comboBox_data_bits.addItem("")
        self.comboBox_data_bits.addItem("")
        self.gridLayout.addWidget(self.comboBox_data_bits, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_connect = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout.addWidget(self.pushButton_connect, 5, 0, 1, 2)
        self.comboBox_Port = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Port.sizePolicy().hasHeightForWidth())
        self.comboBox_Port.setSizePolicy(sizePolicy)
        self.comboBox_Port.setObjectName("comboBox_Port")
        self.gridLayout.addWidget(self.comboBox_Port, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 181, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 24, 151, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_rev_ascii = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_rev_ascii.setObjectName("radioButton_rev_ascii")
        self.gridLayout_2.addWidget(self.radioButton_rev_ascii, 0, 0, 1, 1)
        self.radioButton_rev_hex = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_rev_hex.setObjectName("radioButton_rev_hex")
        self.gridLayout_2.addWidget(self.radioButton_rev_hex, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.comboBox_rev_buff_size = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_rev_buff_size.setObjectName("comboBox_rev_buff_size")
        self.comboBox_rev_buff_size.addItem("")
        self.comboBox_rev_buff_size.addItem("")
        self.comboBox_rev_buff_size.addItem("")
        self.comboBox_rev_buff_size.addItem("")
        self.comboBox_rev_buff_size.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_rev_buff_size, 1, 1, 1, 1)
        self.checkBox_save_file = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_save_file.setObjectName("checkBox_save_file")
        self.gridLayout_2.addWidget(self.checkBox_save_file, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.pushButton_rev_clear = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_rev_clear.setObjectName("pushButton_rev_clear")
        self.gridLayout_2.addWidget(self.pushButton_rev_clear, 3, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 181, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 22, 151, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton_send_ascii = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_send_ascii.setObjectName("radioButton_send_ascii")
        self.gridLayout_5.addWidget(self.radioButton_send_ascii, 0, 0, 1, 1)
        self.radioButton_send_hex = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_send_hex.setObjectName("radioButton_send_hex")
        self.gridLayout_5.addWidget(self.radioButton_send_hex, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_send_clear = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_send_clear.setObjectName("pushButton_send_clear")
        self.gridLayout_5.addWidget(self.pushButton_send_clear, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 0, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(220, 10, 491, 331))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowser_rev = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_rev.setGeometry(QtCore.QRect(0, 40, 481, 281))
        self.textBrowser_rev.setObjectName("textBrowser_rev")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(320, 10, 151, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox_encode = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_encode.setObjectName("comboBox_encode")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_encode, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(220, 360, 491, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget4.setGeometry(QtCore.QRect(22, 22, 461, 81))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit_send = QtWidgets.QTextEdit(self.layoutWidget4)
        self.textEdit_send.setObjectName("textEdit_send")
        self.gridLayout_4.addWidget(self.textEdit_send, 0, 0, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_send.sizePolicy().hasHeightForWidth())
        self.pushButton_send.setSizePolicy(sizePolicy)
        self.pushButton_send.setMinimumSize(QtCore.QSize(70, 60))
        self.pushButton_send.setMaximumSize(QtCore.QSize(70, 60))
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout_4.addWidget(self.pushButton_send, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 340, 491, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.label_5.setText(_translate("MainWindow", "停止位"))
        self.comboBox_parity.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_parity.setItemText(1, _translate("MainWindow", "Odd"))
        self.comboBox_parity.setItemText(2, _translate("MainWindow", "Even"))
        self.label_4.setText(_translate("MainWindow", "奇偶校验"))
        self.comboBox_stop_bits.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_stop_bits.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_stop_bits.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_baud_rate.setItemText(0, _translate("MainWindow", "custom"))
        self.comboBox_baud_rate.setItemText(1, _translate("MainWindow", "1200"))
        self.comboBox_baud_rate.setItemText(2, _translate("MainWindow", "2400"))
        self.comboBox_baud_rate.setItemText(3, _translate("MainWindow", "4800"))
        self.comboBox_baud_rate.setItemText(4, _translate("MainWindow", "9600"))
        self.comboBox_baud_rate.setItemText(5, _translate("MainWindow", "14400"))
        self.comboBox_baud_rate.setItemText(6, _translate("MainWindow", "19200"))
        self.comboBox_baud_rate.setItemText(7, _translate("MainWindow", "38400"))
        self.comboBox_baud_rate.setItemText(8, _translate("MainWindow", "56000"))
        self.comboBox_baud_rate.setItemText(9, _translate("MainWindow", "57600"))
        self.comboBox_baud_rate.setItemText(10, _translate("MainWindow", "115200"))
        self.comboBox_baud_rate.setItemText(11, _translate("MainWindow", "128000"))
        self.comboBox_baud_rate.setItemText(12, _translate("MainWindow", "230400"))
        self.comboBox_baud_rate.setItemText(13, _translate("MainWindow", "256000"))
        self.comboBox_baud_rate.setItemText(14, _translate("MainWindow", "460800"))
        self.comboBox_baud_rate.setItemText(15, _translate("MainWindow", "600000"))
        self.comboBox_baud_rate.setItemText(16, _translate("MainWindow", "750000"))
        self.comboBox_baud_rate.setItemText(17, _translate("MainWindow", "921600"))
        self.comboBox_baud_rate.setItemText(18, _translate("MainWindow", "1000000"))
        self.comboBox_baud_rate.setItemText(19, _translate("MainWindow", "1500000"))
        self.label_3.setText(_translate("MainWindow", "数据位"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.comboBox_data_bits.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_data_bits.setItemText(1, _translate("MainWindow", "6"))
        self.comboBox_data_bits.setItemText(2, _translate("MainWindow", "7"))
        self.comboBox_data_bits.setItemText(3, _translate("MainWindow", "8"))
        self.label.setText(_translate("MainWindow", "端口号"))
        self.pushButton_connect.setText(_translate("MainWindow", "连接"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收设置"))
        self.radioButton_rev_ascii.setText(_translate("MainWindow", "ASCII"))
        self.radioButton_rev_hex.setText(_translate("MainWindow", "HEX"))
        self.label_6.setText(_translate("MainWindow", "缓存大小"))
        self.comboBox_rev_buff_size.setItemText(0, _translate("MainWindow", "200K"))
        self.comboBox_rev_buff_size.setItemText(1, _translate("MainWindow", "500K"))
        self.comboBox_rev_buff_size.setItemText(2, _translate("MainWindow", "1M"))
        self.comboBox_rev_buff_size.setItemText(3, _translate("MainWindow", "2M"))
        self.comboBox_rev_buff_size.setItemText(4, _translate("MainWindow", "5M"))
        self.checkBox_save_file.setText(_translate("MainWindow", "接收数据到文件"))
        self.pushButton_rev_clear.setText(_translate("MainWindow", "清除接收区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送设置"))
        self.radioButton_send_ascii.setText(_translate("MainWindow", "ASCII"))
        self.radioButton_send_hex.setText(_translate("MainWindow", "HEX"))
        self.pushButton_send_clear.setText(_translate("MainWindow", "清除发送区"))
        self.groupBox_4.setTitle(_translate("MainWindow", "接收"))
        self.label_7.setText(_translate("MainWindow", "编码格式"))
        self.comboBox_encode.setItemText(0, _translate("MainWindow", "UTF-8"))
        self.comboBox_encode.setItemText(1, _translate("MainWindow", "GB2312"))
        self.comboBox_encode.setItemText(2, _translate("MainWindow", "GDK"))
        self.groupBox_5.setTitle(_translate("MainWindow", "发送"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))

