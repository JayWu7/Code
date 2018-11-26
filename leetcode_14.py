class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return ''

        value = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        special = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        zeros = {1000: 100, 500: 100, 100: 10, 50: 10, 10: 1, 5: 1 }
        divisors = [1000, 500, 100, 50, 10, 5, 1]
        roma_num = ''
        for divisor in divisors:
            if num >= divisor:
                n, num = int(num / divisor), num % divisor
                roma_num = roma_num + value[divisor] * n
                if not num:
                    return roma_num
            if divisor - num < zeros[divisor]:
                roma_num, num = roma_num + special[divisor - zeros[divisor]], num - divisor + zeros[divisor]
            elif divisor - num == zeros[divisor]:
                return roma_num + special[divisor - zeros[divisor]]

        return roma_num

s=Solution()
print(s.intToRoman(1994))