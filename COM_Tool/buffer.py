class Buffer():
    '''
    定义一个类，管理缓存区

    '''
    __buffer = [] # 定义一个缓存区

    __size = 0
    __maxlen = 0
    __lock = False

    def __init__(self, maxlen = 10*1024):
        self.__maxlen = maxlen    

    def setMaxLen(self, maxlen):
        self.__maxlen = maxlen

    def getMaxLen(self):
        return self.__maxlen

    def getSize(self):
        return self.__size

    def pushData(self, data):
        '''
        data 为byte列表类型
        '''
        while(self.__lock):
            pass
        self.__lock = True
        self.__buffer.append(data)
        self.__size += len(data)

        # 当缓存的大小大于设置的最大的长度，将前面的数据删除
        while self.__size > self.__maxlen:
            str = self.__buffer.pop(0)
            self.__size -= len(str)

        self.__lock = False

    def getData(self):
        return self.__buffer