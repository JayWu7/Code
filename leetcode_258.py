class Solution:
    def addDigits(self, num: int) -> int:
        #xunhuan
        str_num = str(num)
        while True:
            sum = 0
            for s in str_num:
                sum += int(s)

            if sum < 10:
                return sum
            else:
                str_num = str(sum)


#找规律做法：
class Solution:
    def addDigits(self, num: int) -> int:
        if 0 == num:
            return 0
        return (num - 1) % 9 + 1