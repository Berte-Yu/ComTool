class Hex_string():
    def byte_to_hexString(self, byte):
        ''' 
        将byte列表转化为HEX型字符串列表:
        [b'haha',b'nihao'] --> ['68', '61', '68', '61']
        '''
        hexString = []
        if len(byte) == 0:
            return hexString
        
        for b in byte:
            s = b.hex()
            for i in range(len(s)):
                if i%2 == 0:
                    hexString.append((s[i]+s[i+1]).upper())

        return hexString

    def byte_to_utf8str(self, byte):
        utf8String = ""
        if len(byte) == 0:
            return utf8String

        bytestr = b''.join(byte)
        try:
            utf8String = bytestr.decode(encoding='utf-8')
        except:
            utf8String += '*'*len(bytestr)

        return utf8String

if __name__ == "__main__":
    a = Hex_string()
    b = bytes('haha',encoding='utf-8')
    c = a.byte_to_hexString(b)
    print(c)

    b = [b'a',b'b',b'c',b'd',b'e']
    print(b)
    c = a.byte_to_utf8str(b)
    print(c)
    pass