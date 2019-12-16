
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        # 思路：先确定第一个和第二个数，然后再进行后面的步骤

        fn_i = 0  # first num end index
        le = len(num)  # length of num
        while fn_i < le - fn_i:
            fn_i += 1
            sn_i = fn_i + 1  # second num end index
            while sn_i - fn_i <= le - sn_i and fn_i <= le - sn_i:
                fn, sn = num[:fn_i], num[fn_i:sn_i]
                s_i = sn_i  # store the end index of second number
                while True:
                    xn = str(int(fn) + int(sn))  # next num
                    xn_i = s_i + len(xn)
                    if num[s_i:xn_i] == xn and (fn[0] != '0' or fn == '0') and (sn[0] != '0' or sn == '0'):
                        fn, sn, s_i = sn, xn, xn_i
                        if s_i == le:
                            return True
                        elif le - s_i < max(len(fn), len(sn)):
                            break
                    else:
                        break

                sn_i += 1

        return False


s = Solution()
s.isAdditiveNumber("0235813")