class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        byte_nums = len(data)

        if not byte_nums:
            return False

        def dec_to_bin(dec):
            bin = ''
            while dec:  # dec != 0
                bin = str(dec % 2) + bin
                dec = dec // 2

            pre = 8 - len(bin)
            if pre:  # 不满8位，前面补0
                bin = '0' * pre + bin
            return bin

        index = 0
        while index < byte_nums:
            num, bin = 0, dec_to_bin(data[index])
            for b in bin:
                if b == '1':
                    num = num + 1
                else:
                    break
            if num > 4 or num == 1:  #utf-8的字符可能长度为1到4字节
                return False
            elif not num:  # num == 0,为1字节字符
                pass
            else:
                if byte_nums - index < num:  #当前剩余数字小于当前n字节的字节数
                    return False
                else:
                    for i in range(num - 1):
                        index = index + 1
                        if dec_to_bin(data[index])[:2] != '10':
                            return False
            index = index + 1
        return True

s = Solution()
print(s.validUtf8([197, 130, 1]))
