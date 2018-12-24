class Solution:
    def myAtoi(self, str):

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        str = str.strip()

        if not str:
            return 0

        first_l = str[0]

        if ord(first_l) in range(48, 58) or first_l in ['+', '-']:

            index = 1
            while index < len(str):
                if ord(str[index]) not in range(48, 58):
                    str = str[:index]
                    break
                index +=1

        else:
            return 0

        if len(str) == 1 and first_l in ['+', '-']:
            return 0

        number = int(str)
        if number > INT_MAX or number < INT_MIN:
            return INT_MAX if number > 0 else INT_MIN
        else:
            return number
