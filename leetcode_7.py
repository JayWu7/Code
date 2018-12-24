class Solution:
    def reverse(self, x):


        str_x = str(x)
        reverse_str_x = str_x[::-1]
        reverse_int = 0
        if (x >= 0):
            reverse_int = int(reverse_str_x)
        else:
            reverse_int = -int(reverse_str_x[:-1])

        if reverse_int >= (2 ** 31) or reverse_int < -(2 ** 31):
            return 0
        else:
            return  reverse_int

