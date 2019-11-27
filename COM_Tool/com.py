import serial
import serial.tools.list_ports
import serial.serialutil
class com(object):
    """串口操作的封装"""
    def __init__(self):
        self.dev = None
        pass

    def com_scan(self):
        # 扫描端口并返回端口
        # 返回 串口设备对象
        dev_list = serial.tools.list_ports.comports()
        return dev_list

    def open(self, _port, _baudrate, _bytesize, _parity, _stopbits):
        if _parity == 'None':
            _parity = serial.serialutil.PARITY_NONE
        elif _parity == 'Odd':
            _parity = serial.serialutil.PARITY_ODD
        elif _parity == 'Even':
            _parity = serial.serialutil.PARITY_EVEN
        self.dev = serial.Serial(port=_port, baudrate=_baudrate, bytesize=_bytesize, parity=_parity, stopbits=_stopbits)

    def close(self):
        self.dev.close()

if __name__ == "__main__":
    dev = com()
    list = dev.com_scan()
    
    print(list)