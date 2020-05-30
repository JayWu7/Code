class Solution(object):
    def __init__(self):
        self.result_all = None
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = None

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.result_all = []
        self.visited = [0 for _ in range(len(self.nums))]
        self.dfs(num, 0, 0)
        return self.result_all

    def dfs(self, num, step, start):
        if step == num:
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            if not self.calc_sum(self.visited):
                self.visited[i] = 0
                continue
            self.dfs(num, step + 1, i + 1)
            self.visited[i] = 0
        return

    def calc_sum(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        return 0 <= sum_h <= 11 and 0 <= sum_m <= 59

    def handle_date(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        result = "" + str(sum_h) + ":"
        if sum_m < 10:
            result += "0" + str(sum_m)
        else:
            result += str(sum_m)
        return result