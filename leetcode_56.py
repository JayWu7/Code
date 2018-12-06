# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # def __cmp__(self, other):
    #     if self.start <= other.start:
    #         (x1, y1), (x2, y2) = (self.start, self.end), (other.start, other.end)
    #     else:
    #         (x1, y1), (x2, y2) = (other.start, other.end), (self.start, self.end)
    #     if y1 < x2:
    #         return False
    #     elif x1 <= x2 < y2 <= y1:
    #         return [x1, y1]
    #     else:
    #         return [x1, y2]


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        def cmp(current, other):
            if current.end < other.start:
                return False
            elif current.start <= other.start <= other.end <= current.end:
                pass
            else:
                current.end = other.end
            return current

        intervals.sort(key=lambda interval: interval.start)
        new_intervals, interval = [], intervals[0]
        for i in range(1,len(intervals)):
            result = cmp(interval, intervals[i])
            if not result:
                new_intervals.append([interval.start, interval.end])
                interval = intervals[i]
            else:
                interval = result
                continue
        new_intervals.append([interval.start, interval.end])
        return new_intervals

import profile
s = Solution()
a = Interval(1, 3)
b = Interval(2, 6)
c = Interval(8, 10)
d = Interval(15, 18)
print(s.merge([a, b, c, d]))

#Excellent code
# class Solution:
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         if len(intervals)==0:
#             return []
#         intervals.sort(key=lambda x:x.start)
#         l = intervals[0].start
#         r = intervals[0].end
#         ans = []
#         for i in intervals:
#             if r >= i.start:
#                 r = max(r,i.end)
#             else:
#                 ans.append(Interval(l,r))
#                 l = i.start
#                 r = i.end
#         ans.append(Interval(l,r))
#         return ans
