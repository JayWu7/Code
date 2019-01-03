class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for num in range(1, n + 1):
            # if num % 3 == 0 and num % 5 ==0:
            if num % 15 == 0:
                res.append('FizzBuzz')
            elif num % 3 == 0:
                res.append('Fizz')
            elif num % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(num))
        return res


# method 2   计数，每到3 或5 或 15 处理一下
class Solution(object):
    def fizzBuzz(self, n):
        count3 = count5 = count15 = 0
        res = []
        for num in range(1, n + 1):
            count3 += 1
            count5 += 1
            count15 += 1
            if count15 == 15:
                res.append('FizzBuzz')
                count3 = count5 = count15 = 0
                continue
            elif count3 == 3:
                res.append('Fizz')
                count3 = 0
            elif count5 == 5:
                res.append('Buzz')
                count5 = 0
            else:
                res.append(str(num))
        return res


#quick code
class Solution(object):
    def fizzBuzz(self, n):
        L = []
        for x in range(1, n + 1):
            tmp = ''
            if x % 3 == 0:
                if x % 5 == 0:
                    tmp += 'FizzBuzz'
                else:
                    tmp += 'Fizz'
            else:
                if x % 5 == 0:
                    tmp += 'Buzz'
                else:
                    tmp += str(x)
            L.append(tmp)
        return L