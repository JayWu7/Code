class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        '''
            思路：
                首先判断倒数第二个bit是不是1，如果是0，则返回True
                否则，问题转化为判断bits[:-2]是不是一个正确编码的问题
                如果是，返回False，否则 返回True
        :param bits:
        :return:
        '''
        le = len(bits)
        if le == 1 or bits[-2] == 0:
            return True

        i = 0
        while i < le - 2:
            if bits[i] == 1:  #must combine next bit
                i += 2
            else:
                i += 1

        return i != le - 2

