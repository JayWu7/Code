class Solution:
    def get_factorial(self, num):
        i, factorial = 1, 1
        while i <= num:
            factorial = factorial * i
            i = i + 1
        return factorial

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = ''

        def gener_permu(numbers, k):
            nonlocal num
            if len(numbers) == 1:
                num = num + str(numbers[0])
                return
            factorial = self.get_factorial(len(numbers) - 1)  # 获得n-1的阶乘
            sequence = k / factorial  # 判断当前位置应该是几
            if sequence == int(sequence):  # sequence不是整数
                sequence = sequence - 1
            sequence = int(sequence)
            str_n = numbers.pop(sequence)
            num = num + str(str_n)
            k = k - factorial * sequence
            gener_permu(numbers, k)

        gener_permu([i + 1 for i in range(n)], k)
        return num
