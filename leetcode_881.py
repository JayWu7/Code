# class Solution:
#     def numRescueBoats(self, people, limit: int) -> int:
#         #  sort, greedy, double pointer
#         people.sort(reverse=True)
#         length = len(people)
#         fir = 0
#         people_flag = [True for _ in range(length)]  # store the info of if this man has been transported
#         ans = 0
#         while fir < length:
#             if people_flag[fir]:
#                 if people[fir] == limit:
#                     ans += 1
#                 elif people[fir] < limit:
#                     sec = fir + 1
#                     left_limit = limit - people[fir]
#                     while sec < length:
#                         if people[sec] <= left_limit and people_flag[sec]:
#                             people_flag[sec] = False
#                             break
#                         sec += 1
#                     ans += 1
#
#             fir += 1
#
#         return ans

# 优化
class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        #  sort, greedy, double pointer
        people.sort(reverse=True)
        length = len(people)
        fir, sec = 0, length - 1
        people_flag = [True for _ in range(length)]  # store the info of if this man has been transported
        ans = 0
        while fir < length:
            if people_flag[fir]:
                if people[fir] == limit:
                    ans += 1
                    people_flag[fir] = False
                elif people[fir] < limit:
                    ans += 1
                    if people_flag[sec] and people[fir] + people[sec] <= limit:
                        people_flag[sec] = False
                        sec -= 1
            fir += 1

        return ans


# 再优化
class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        ans = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
            ans += 1

        return ans


s = Solution()
print(s.numRescueBoats([5, 1, 7, 4, 2, 4], 7))
