class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        #思路： 遍历logs，如果是start加入栈，是end，pop出栈顶元素，计算时间
        time: 35 min
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0 for _ in range(n)]

        for log in logs:
            log = log.split(':')
            log[0], log[2] = int(log[0]), int(log[2])
            if log[1] == 'start':
                if stack:
                    res[stack[-1][0]] += log[2] - stack[-1][1]
                stack.append([log[0], log[2]])
            else:
                cur = stack.pop()
                res[cur[0]] += log[2] - cur[1] + 1
                if stack:
                    stack[-1][1] = log[2] + 1
        return res

# s = Solution()
# s.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
