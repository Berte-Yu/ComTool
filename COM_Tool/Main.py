# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
import sys
import Main_form
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
import com

class Main_form_UI(QtWidgets.QMainWindow, QtWidgets.QWidget, Main_form.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_form_UI, self).__init__(parent)
        self.setupUi(self)
        
        self._init_param()
        self._init_event()

    def _init_event(self):
        # 初始化各个控件的信号和槽
         # 将此定时器的超时连接到扫描端口方法上
        self.scan_uart_timer.timeout.connect(self.scan_uart)
        # 设置定时器的间隔时间并启动定时器
        self.scan_uart_timer.start(500)

        # 连接按钮的槽函数
        self.pushButton_connect.clicked.connect(self.connecthandle)
        

    def _init_param(self):
        # 初始化参数
        self.ComTool_status = {
                # 串口的链接状态
                'isConnect' : False,
                'dev_status': False,
                # 当前选中的串口列表名字
                'dev_name' : '',
                # 波特率
                'baud_rate' : '115200',
                # 数据位
                'data_bits' : '8',
                # 奇偶校验位
                'parity'    : 'None',
                # 停止位
                'stop_bits' : '1',
                # 接收格式
                'recv_format': 'ASCII',
                # 发送格式
                'send_format' : 'ASCII',
                # 接收区缓存大小
                'recv_buff_size' : '200K',
                # 是否将接收的数据保存到文件
                'is_recv_save_2_file' : False,
                # 接收显示区的编码格式
                'encoding_format' : 'UTF-8',
            }

        self.com_dev = com.com()
        self.com_dev_list = []

        self._set_def_com_status()

        # 初始化一个定时器
        self.scan_uart_timer = QTimer()

        # 设置默认的接收和发送的格式
        if self.ComTool_status['recv_format'] == 'ASCII':
            self.radioButton_rev_ascii.setChecked(True)
        else:
            self.radioButton_rev_hex.setChecked(True)

        if self.ComTool_status['send_format'] == 'ASCII':
            self.radioButton_send_ascii.setChecked(True)
        else:
            self.radioButton_send_hex.setChecked(True)
        

    def _set_def_com_status(self):
        # 设置默认的串口状态
        self.comboBox_baud_rate.setCurrentText(self.ComTool_status['baud_rate'])
        self.comboBox_data_bits.setCurrentText(self.ComTool_status['data_bits'])
        self.comboBox_parity.setCurrentText(self.ComTool_status['parity'])
        self.comboBox_stop_bits.setCurrentText(self.ComTool_status['stop_bits'])

    def _get_current_com_status(self):
        # 获取当前界面设置的串口状态
        self.ComTool_status['baud_rate'] = self.comboBox_baud_rate.currentText()
        self.ComTool_status['data_bits'] = self.comboBox_data_bits.currentText()
        self.ComTool_status['parity']    = self.comboBox_parity.currentText()
        self.ComTool_status['stop_bits'] = self.comboBox_stop_bits.currentText()
        self.ComTool_status['dev_name']  = self.comboBox_Port.currentText()
        
    def _get_comboBox_items(self, comboBox):
        # 获取comboBox当前所有的下拉列表内容
        cmbBox_list = []

        for cmbBox in range(comboBox.count()):
            cmbBox_list.append(comboBox.itemText(cmbBox))
        
        return cmbBox_list

    def scan_uart(self):
        # 间隔500ms进行扫描端口
        pc_com_name_list = []

        self.com_dev_list = self.com_dev.com_scan()
         
        for pc_dev in self.com_dev_list:
            pc_com_name_list.append(pc_dev.device)

        # 将扫描出的端口显示到界面
        gui_com_dev_list = self._get_comboBox_items(self.comboBox_Port)

        if pc_com_name_list != gui_com_dev_list:
            self.comboBox_Port.clear()
            self.comboBox_Port.addItems(pc_com_name_list)
            
    def connecthandle(self):
        # 点击按键后的操作
        
        # 更改链接状态
        self.ComTool_status['isConnect'] = not self.ComTool_status['isConnect']

        if self.ComTool_status['isConnect'] is True:
            # 获取状态
            self._get_current_com_status()
            
            if self.ComTool_status['dev_name'] == '':
                # 当前没有选中任何设备，直接弹窗报错
                self.ComTool_status['isConnect'] = False
                QtWidgets.QMessageBox.warning(self,'串口设备选择错误', '串口设备没有插入。', QtWidgets.QMessageBox.Ok)
                return

            # 打开串口
            try:
                self.com_dev.open(self.ComTool_status['dev_name'],
                              int(self.ComTool_status['baud_rate']),
                              int(self.ComTool_status['data_bits']),
                              self.ComTool_status['parity'],
                              int(self.ComTool_status['stop_bits']))
            except:
                self.ComTool_status['isConnect'] = False
                QtWidgets.QMessageBox.warning(self,'串口设备错误', '串口设备被占用。', QtWidgets.QMessageBox.Ok)
                return

            self.ComTool_status['dev_status'] = True
            
            # 停止串口扫描的定时器
            self.scan_uart_timer.stop()

            # 改变连接按键的显示文本
            self.pushButton_connect.setText('断开')

        else:
            # 设置定时器的间隔时间并启动定时器
            self.scan_uart_timer.start(500) 
            self.pushButton_connect.setText('连接')
            
            # 关闭串口
            if self.ComTool_status['dev_status'] == True:
                self.ComTool_status['dev_status'] = False
                self.com_dev.close()

def mywindow():
    mywindow = Main_form_UI()
    mywindow.show()
    return mywindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myobj = mywindow()
    sys.exit(app.exec_())
