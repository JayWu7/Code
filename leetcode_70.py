# method 1  使用递归（方法超时）
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        思路: 爬上n阶台阶的方法数等于爬上n-1阶台阶的方法数 加上 爬上n-2阶台阶的方法数 (很明显，这是一个斐波那契数列问题)
        """
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# method 2
class Solution(object):
    def climbStairs(self, n):
        from math import factorial
        """
        :type n: int
        :rtype: int
        思路： 把问题转化为 1和2 的组合排列问题
        n阶台阶的爬行方法，是爬a次1阶加爬b次2阶，满足 a+2b = n, a = n - 2b, 所以b的取值范围为：[0,n//2]
        算出所有可能的a和b的方案
        然后就是排列问题，算出a个1阶和b个2阶的所有可能排列方案
        推导可得 所有的排列方案为 (a+b)! / a! * b!
        """
        sum = 1  # 第一种方法为全为1
        for b in range(1, n // 2 + 1):
            a = n - 2 * b
            sum += (factorial(a + b) / (factorial(a) * factorial(b)))
        return sum


# metnod 3   斐波那契数列求解
class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        num1, num2 = 1, 2
        for _ in range(2, n):
            num1, num2 = num2, num1 + num2
        return num2
