# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
import sys
import Main_form
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
import com
import Runthread
import Hex_string
import os
import time
import json
import datetime

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
        
        # 发送按钮的槽函数
        self.pushButton_send.clicked.connect(self.sendButtonHandle)

        # 连接接收缓存最大行
        self.comboBox_rev_buff_size.currentIndexChanged.connect(self.setRevBuffSize)

        # 清除接收区按钮
        self.pushButton_rev_clear.clicked.connect(self.clearRx)

        # 清除发送区按钮
        self.pushButton_send_clear.clicked.connect(self.clearTx)

        # 设置保存文件的信号
        self.checkBox_save_file.stateChanged.connect(self.save_file)

        # 设置发送模式的信号
        self.checkBox_send_hex.toggled.connect(self.send_mode)

        # 设置编码方式的信号
        self.comboBox_encode.currentIndexChanged.connect(self.changeEncode)

        self.tool_mult_string_send.triggered.connect(self.multi_string_send)


    def _init_param(self):
        # 初始化参数
        self.ComTool_status = {
                # 串口的链接状态
                'isConnect' : False,
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
                'recv_buff_size' : '1000',
                # 是否将接收的数据保存到文件
                'is_recv_save_2_file' : False,
                # 接收显示区的编码格式
                'encoding_format' : 'ASCII',
            }

        # 加载配置文件的路径
        self.param_file_path = os.path.join(os.path.abspath('.'), 'data', 'param.dat')

        self.recv_file_path = os.path.join(os.path.abspath('.'),'RecvFile')

        self.com_dev = com.com()

        self.com_dev_list = []

        # 初始化一个定时器
        self.scan_uart_timer = QTimer()

        self.__load_param_file()

        self._set_def_com_status()

        # 实例化一个字符转换类
        self.hex_handler = Hex_string.Hex_string()

        # 设置接收区最大行数
        self.plainTextEdit_rev.setMaximumBlockCount(int(self.ComTool_status['recv_buff_size']))

        # 保存文件句柄
        self.RecvDataFile = None

    def __load_param_file(self):
        # 加载参数文件
        if not os.path.exists(self.param_file_path):
            #没有参数文件
            with open(self.param_file_path,'w',encoding='utf-8') as f:
                # 将默认参数导入文件
                f.write(json.dumps(self.ComTool_status, indent=4)) 
                f.close()
        with open(self.param_file_path,'r',encoding='utf-8') as f:
            self.ComTool_status = json.loads(f.read(), encoding='utf-8')
            f.close()
        pass

    def _set_def_com_status(self):
        # 设置默认的串口状态
        self.comboBox_baud_rate.setCurrentText(self.ComTool_status['baud_rate'])
        self.comboBox_data_bits.setCurrentText(self.ComTool_status['data_bits'])
        self.comboBox_parity.setCurrentText(self.ComTool_status['parity'])
        self.comboBox_stop_bits.setCurrentText(self.ComTool_status['stop_bits'])

        # 设置接收框的最大行数
        self.comboBox_rev_buff_size.setCurrentText(self.ComTool_status['recv_buff_size'])

        # 设置编码方式
        self.comboBox_encode.setCurrentText(self.ComTool_status['encoding_format'])

        # 设置默认的接收和发送的格式
        if self.ComTool_status['recv_format'] == 'ASCII':
            self.checkBox_recv_hex.setChecked(False)
        else:
            self.checkBox_recv_hex.setChecked(True)

        if self.ComTool_status['send_format'] == 'ASCII':
            self.checkBox_send_hex.setChecked(False)
        else:
            self.checkBox_send_hex.setChecked(True)

        # 设置是否保存到文件的控件状态
        if self.ComTool_status['is_recv_save_2_file'] == False:
            self.checkBox_save_file.setChecked(False)
        else:
            self.checkBox_save_file.setChecked(True)

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
        # 点击连接按键后的操作

        if self.ComTool_status['isConnect'] is False:
            # 获取状态
            self._get_current_com_status()
            
            if self.ComTool_status['dev_name'] == '':
                # 当前没有选中任何设备，直接弹窗报错
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
                QtWidgets.QMessageBox.warning(self,'串口设备错误', '串口设备被占用。', QtWidgets.QMessageBox.Ok)
                return

            
            # 停止串口扫描的定时器
            self.scan_uart_timer.stop()

            # 改变连接按键的显示文本
            self.pushButton_connect.setText('断开')

            # 设置连接状态
            self.ComTool_status['isConnect'] = True

            # 将串口控件参数控件设置为只读
            self.comboBox_Port.setDisabled(True)
            self.comboBox_baud_rate.setDisabled(True)
            self.comboBox_data_bits.setDisabled(True)
            self.comboBox_parity.setDisabled(True)
            self.comboBox_stop_bits.setDisabled(True)

            # 创建串口接收和发送的线程
            self.thread_rx = Runthread.Runthread(self.com_dev.com_rxHandler,name='rxHandler')
            self.thread_tx = Runthread.Runthread(self.com_dev.com_txHandler,name='txHandler')
            self.thread_rxData = Runthread.Runthread(self.rxDataHandler,name='rxdataHandler')
            self.thread_rxData.sendmsg.connect(self.display) # 将接收数据处理的线程信号连接到此处
            self.thread_rx.start()
            self.thread_tx.start()
            self.thread_rxData.start()

        else:
            self.thread_rx.stop()
            self.thread_tx.stop()
            self.thread_rxData.stop()

            self.thread_rx.join()
            self.thread_tx.join()
            self.thread_rxData.join()

            self.thread_rxData.sendmsg.disconnect(self.display)

            # 关闭串口
            self.com_dev.close()

            # 将串口控件参数控件设置为只读
            self.comboBox_Port.setDisabled(False)
            self.comboBox_baud_rate.setDisabled(False)
            self.comboBox_data_bits.setDisabled(False)
            self.comboBox_parity.setDisabled(False)
            self.comboBox_stop_bits.setDisabled(False)

            # 设置定时器的间隔时间并启动定时器
            self.scan_uart_timer.start(500) 
            self.pushButton_connect.setText('连接')
            
            # 设置连接状态
            self.ComTool_status['isConnect'] = False

    def sendButtonHandle(self):
        # 获取发送区的内容
        sendtext = self.textEdit_send.toPlainText()

        if len(sendtext) != 0:
            if self.checkBox_send_hex.isChecked()==False:
                if self.comboBox_encode.currentText() == 'UTF-8':
                    self.com_dev.write(sendtext.encode(encoding='utf-8'))
                elif self.comboBox_encode.currentText() == 'ASCII':
                    try:
                        self.com_dev.write(sendtext.encode(encoding='ascii'))
                    except UnicodeEncodeError:
                        QtWidgets.QMessageBox.warning(self,'发送框：','当前字符无法以ascii发送！')

                elif self.comboBox_encode.currentText() == 'GBK':
                    self.com_dev.write(sendtext.encode(encoding='gbk'))
            else:
                # 以HEX方式发送
                try:
                    byte_str = self.hex_handler.str2Hex(sendtext)
                    self.com_dev.write(byte_str)
                except:
                    QtWidgets.QMessageBox.warning(self,'Hex：','输入非法！')
                
    def send_mode(self):
        sendtext = self.textEdit_send.toPlainText()
        if len(sendtext) == 0:
            return

        if self.checkBox_send_hex.isChecked() == False:
            # hex-->str    
            try:
                t = []
                b = self.hex_handler.str2Hex(sendtext)
                t.append(b)
                if self.comboBox_encode.currentText() == 'UTF-8':
                    s = self.hex_handler.byte_to_string(t,'utf-8')
                elif self.comboBox_encode.currentText() == 'ASCII':
                    s = self.hex_handler.byte_to_string(t,'ascii')
                elif self.comboBox_encode.currentText() == 'GBK':
                    s = self.hex_handler.byte_to_string(t,'gbk')
                
                self.textEdit_send.setPlainText(s)
            except:
                QtWidgets.QMessageBox.warning(self,'Hex：','输入非法！')
                self.checkBox_send_hex.toggled.disconnect(self.send_mode)
                self.checkBox_send_hex.setChecked(True)
                self.checkBox_send_hex.toggled.connect(self.send_mode)
        else:
            # str --> hex
            bytestr = []
            display_str = ''

            try:
                if self.comboBox_encode.currentText() == 'UTF-8':
                    bytestr.append(sendtext.encode(encoding='utf-8'))
                elif self.comboBox_encode.currentText() == 'ASCII':
                    bytestr.append(sendtext.encode(encoding='ascii'))
                elif self.comboBox_encode.currentText() == 'GBK':
                    bytestr.append(sendtext.encode(encoding='gbk'))
            except:
                QtWidgets.QMessageBox.warning(self,'String：','无法以当前编码方式解码，请修改编码方式！')
                self.checkBox_send_hex.toggled.disconnect(self.send_mode)
                self.checkBox_send_hex.setChecked(False)
                self.checkBox_send_hex.toggled.connect(self.send_mode)
                return

            str_hex = self.hex_handler.byte_to_hexString(bytestr)
            for s in str_hex:
                display_str += s+' '
            self.textEdit_send.setPlainText(display_str)

    def setRevBuffSize(self):
        self.ComTool_status['recv_buff_size'] = self.comboBox_rev_buff_size.currentText()
        print('设置最大的显示行数'+self.ComTool_status['recv_buff_size'])
        self.plainTextEdit_rev.setMaximumBlockCount(int(self.ComTool_status['recv_buff_size']))
        
    def clearRx(self):
        self.plainTextEdit_rev.clear()

    def clearTx(self):
        self.textEdit_send.clear()

    def changeEncode(self):
        self.ComTool_status['encoding_format'] = self.comboBox_encode.currentText()

    def save_file(self):
        if self.checkBox_save_file.isChecked():
            if self.RecvDataFile != None:
                self.RecvDataFile.close()
                self.RecvDataFile = None

            file_path = os.path.join(self.recv_file_path,datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))+'.DAT'
            print(file_path)
            self.RecvDataFile = open(file_path,'a',encoding='utf-8')
            QtWidgets.QMessageBox.information(self,'文件保存路径','之后接收到的数据都将保存在'+file_path+' !')
        else:
            if self.RecvDataFile != None:
                self.RecvDataFile.close()
                self.RecvDataFile = None

    def rxDataHandler(self,sendmsg = None):
        # 从接收缓存中获取数据进行处理
        rx_data = []
        

        '''
        # 队列中有值
        while not self.com_dev.rx_queue.empty():
            rx_data.append(self.com_dev.rx_queue.get_nowait())

        if len(rx_data) != 0:

            if self.checkBox_recv_hex.isChecked():
                display_str = ''
                # 将接收到的数据按照hex格式显示
                hex_rx_data = self.hex_handler.byte_to_hexString(rx_data)

                # 将字符串追加到显示区
                for str in hex_rx_data:
                    display_str += str+' '

                sendmsg.emit(display_str) # 将数据发送到显示函数中进行显示
            else:
                # 将接收的数据以ascii字符串的形式保存
                if self.comboBox_encode.currentText() == 'UTF-8':
                    utf8_rx_data = self.hex_handler.byte_to_string(rx_data,'utf-8')
                    sendmsg.emit(utf8_rx_data) # 将数据发送到显示函数中进行显示
                elif self.comboBox_encode.currentText() == 'ASCII':
                    ascii_rx_data = self.hex_handler.byte_to_string(rx_data,'ascii')
                    sendmsg.emit(ascii_rx_data) # 将数据发送到显示函数中进行显示
                elif self.comboBox_encode.currentText() == 'GBK':
                    gdk_rx_data = self.hex_handler.byte_to_string(rx_data, 'gbk')
                    sendmsg.emit(gdk_rx_data) # 将数据发送到显示函数中进行显示
        else:
            time.sleep(0.08)

        '''

    def display(self, msg):
        self.plainTextEdit_rev.insertPlainText(msg)
        
        # 判断是否将显示的数据存入文件
        if self.RecvDataFile != None:
            self.RecvDataFile.write(msg)
        self.plainTextEdit_rev.moveCursor(self.plainTextEdit_rev.textCursor().End)

    def closeEvent(self, cls):
        # 正常退出事件
        if self.ComTool_status['isConnect'] is True:
            self.connecthandle()

        if self.RecvDataFile != None:
            self.RecvDataFile.close()
            self.RecvDataFile = None
        
        with open(self.param_file_path,'w',encoding='utf-8') as f:
            f.write(json.dumps(self.ComTool_status, indent=4))
            f.close()
        return super().closeEvent(cls)

    def multi_string_send(self):
        print('菜单栏被点击')

def mywindow():
    mywindow = Main_form_UI()
    mywindow.show()
    return mywindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myobj = mywindow()
    sys.exit(app.exec_())
