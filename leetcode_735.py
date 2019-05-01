class Solution:
    '''
    思路： 使用栈，只有在栈顶为正，且当前要进来的元素为负时，才会爆炸
    # time: 20 min
    '''

    def asteroidCollision(self, asteroids):
        stack = []

        for asd in asteroids:
            while stack and stack[-1] > 0 and asd < 0:
                new = stack[-1] + asd
                if new < 0:
                    stack.pop()
                elif new == 0:
                    stack.pop()
                    break
                else:
                    break
            else: #正常退出循环，没有break
                stack.append(asd)

        return stack