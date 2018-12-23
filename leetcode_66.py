class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        思路：  从列表最后往前遍历，每次在当前位置加1，如果加完后当前值不大于10，就退出循环。否则当前值变个位数,index - 1
        """
        index = len(digits) - 1
        while index > -1:
            digits[index] += 1
            if digits[index] == 10:
                digits[index] = 0
                index -= 1
            else:
                break
        else:  # 正常退出循环，要在最前面加一个1
            digits.insert(0, 1)
        return digits

#method 2
class Solution:
    def plusOne(self, digits):
        str_digits = [str(digit) for digit in digits]
        number = int(''.join(str_digits))
        number = number + 1
        str_number = str(number)
        res = [int(num) for num in str_number]
        return res