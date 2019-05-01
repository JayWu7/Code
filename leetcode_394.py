class Solution:
    '''
    #思路： 利用两个栈：一个用来储存数值，一个用来储存字符串
        迭代s，具体思路见代码
    time： 30min
    '''
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        res, i, length = '', 0, len(s)
        while i < length:
            if s[i].isdigit():
                start = i
                while s[i + 1].isdigit():
                    i += 1
                num_stack.append(int(s[start:i + 1]))
            elif s[i] == '[':
                str_stack.append('')
            elif s[i] == ']':
                st = str_stack.pop()
                n = num_stack.pop()
                cur = st * n
                if str_stack:
                    str_stack[-1] = str_stack[-1] + cur
                else:
                    res = res + cur
            else:
                if str_stack:
                    str_stack[-1] = str_stack[-1] + s[i]
                else:
                    res = res + s[i]
            i += 1
        return res
