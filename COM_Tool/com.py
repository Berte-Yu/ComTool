import serial
import serial.tools.list_ports
import serial.serialutil
from queue import Queue
import time

class com(object):
    """串口操作的封装"""
    def __init__(self):
        # 定义一个串口对象
        self.dev = None

        # 定义接收队列
        self.rx_queue = Queue()

        # 定义发送队列
        self.tx_queue = Queue()

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
        self.dev = serial.Serial(port=_port, baudrate=_baudrate, bytesize=_bytesize, parity=_parity, stopbits=_stopbits, timeout=0.5)
        
    def close(self):
        self.dev.close()
        self.dev = None

    def com_txHandler(self,sendmsg=None):

        # 由线程去调用，判断队列里是否有值并发送或者接收到队列里
        if self.dev == None:
            return
        
        if(not self.tx_queue.empty()):
            try:
                self.dev.write(self.tx_queue.get_nowait())
            except:
                return
        else:
            time.sleep(0.05)

    def com_rxHandler(self,sendmsg=None):
        read_num = self.dev.in_waiting
        if read_num == 0:
            time.sleep(0.05)
            return

        try:
            read_data = self.dev.read(read_num)
        except:
            return
        
        self.rx_queue.put_nowait(read_data)

    def write(self, data):
        # date是byte类型的列表
        return self.tx_queue.put_nowait(data)

    def read(self, size):
        # 返回的是byte类型的列表
        read_data = []
        while(size):
            if not self.rx_queue.empty():
                read_data += self.rx_queue.get_nowait()
                size-=1
            else:
                break
        
        if len(read_data) == 0:
            return None
        else:
            return read_data


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    import time

    def txhand(a):
        while(1):
            a.com_txHandler()
            time.sleep(0.01)
    def rxhand(a):
        while(1):
            a.com_rxHandler()
            time.sleep(0.01)

    threadPool = ThreadPoolExecutor(max_workers=2,thread_name_prefix='test_com_')

    dev = com()
    list = dev.com_scan()
    
    dev.open(list[0].device,115200,8,'None',1)

    future = threadPool.submit(txhand,dev)
    future1 = threadPool.submit(rxhand,dev)
    dev.write(bytes("haha",encoding='utf-8'))
    
    while(1):
        a = dev.read(10)
        if a != None:
            print(a)
            dev.write(a)
        time.sleep(0.01)

    