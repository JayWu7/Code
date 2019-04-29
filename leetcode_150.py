class Solution:
    def evalRPN(self, tokens):
        # 思路： 栈来储存数据，如果是运算符，则取栈顶两个元素来进行计算，计算结果加入栈顶
        stack = []
        operations = {'+','-','*','/'}
        def helper(b,a,op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return int(a / b)

        for c in tokens:
            if c in operations:
                stack.append(helper(stack.pop(),stack.pop(),c))
            else:
                stack.append(int(c))

        return stack[0]



# 改写加快版：
class Solution:
    def evalRPN(self, tokens):
        # 思路： 栈来储存数据，如果是运算符，则取栈顶两个元素来进行计算，计算结果加入栈顶
        stack = []
        operations = {'+','-','*','/'}

        for c in tokens:
            if c in operations:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    d = a + b
                elif c == '-':
                    d = a - b
                elif c == '*':
                    d = a * b
                else:
                    d = int(a / b)
                stack.append(d)
            else:
                stack.append(int(c))

        return stack[0]



