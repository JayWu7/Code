# method 1 超时
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0 for _ in T]
        for i, t in enumerate(T):
            day = 0
            while stack and stack[-1][1] < t:
                day += 1
                res[stack.pop()[0]] += day
            for s in stack:
                res[s[0]] += day
            stack.append([i, t])
        for s in stack:
            res[s[0]] = 0
        return res


# method2
class Solution(object):
    def dailyTemperatures(self, T):
        """
        思路： 注意下标差即为两个温度相隔的天数
        time: 55min
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        # res = [0 for _ in T]   #not fast
        res = []
        for i, t in enumerate(T):
            res.append(0)
            while stack and stack[-1][1] < t:
                ind = stack.pop()[0]
                res[ind] = i - ind
            stack.append([i, t])
        return res
