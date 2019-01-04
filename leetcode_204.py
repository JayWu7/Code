# method 1   代码正确，但超时（O(n²)）
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        思路： 定义是否是质数函数，然后遍历小于n的数
        """

        def is_prime(num):
            if num <= 1:
                return True
            if num == 2:
                return True
            elif num % 2 == 0:
                return False
            else:
                for n in range(3, int(num ** 0.5) + 1, 2):  # 直接从3开始，步长为2， 因为如果num不能被2整除，则肯定不能被2的倍数整除
                    if num % n == 0:
                        return False
                return True

        if n < 2:
            return 0
        elif n == 2:
            return 1
        total_primes = 1
        for num in range(3, n, 2):
            if is_prime(num):
                total_primes += 1
        return total_primes


# method 2    超时
class Solution(object):
    def countPrimes(self, n):
        def is_prime(num):
            if num <= 1:
                return True
            if num == 2:
                return True
            elif num % 2 == 0:
                return False
            else:
                for n in range(3, int(num ** 0.5) + 1, 2):  # 直接从3开始，步长为2， 因为如果num不能被2整除，则肯定不能被2的倍数整除
                    if num % n == 0:
                        return False
                return True

        num_list = [num for num in range(n)]
        total_pri = 0
        index = 2
        while index < n:
            if num_list[index]:  # 不为0
                cur = num_list[index]
                if is_prime(cur):  # 是质数，用它来去除它的倍数
                    total_pri += 1
                    for mul in range(2, n // cur):
                        num_list[mul * cur] = 0
            index += 1
        return total_pri

from collections import deque
# method 3
class Solution(object):
    def countPrimes(self, n):
        def is_prime(num):
            if num <= 1:
                return True
            if num == 2:
                return True
            elif num % 2 == 0:
                return False
            else:
                for n in range(3, int(num ** 0.5) + 1, 2):  # 直接从3开始，步长为2， 因为如果num不能被2整除，则肯定不能被2的倍数整除
                    if num % n == 0:
                        return False
                return True

        if n <= 2:
            return 0
        total_pri = 1
        num_deq = deque([num for num in range(3, n, 2)])
        while num_deq:
            cur = num_deq.popleft()
            if is_prime(cur):  # 当前是质数
                total_pri += 1
                for mul in range(cur + 1, n // cur):
                    if mul * cur in num_deq:
                        num_deq.remove(mul * cur)
        return total_pri


#excellent code
class Solution(object):

    def countPrimes(self, n):
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * len(prime[i * i:n:i])
        return sum(prime)