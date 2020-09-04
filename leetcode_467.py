# class Solution:
#     def findSubstringInWraproundString(self, p: str) -> int:
#         alpha = 'abcdefghijklmnopqrstuvwxyza'
#         dp_dict = {s: 0 for s in alpha}
#         conn_set = {alpha[i] + alpha[i + 1] for i in range(len(alpha) - 1)}
#         pre = 0
#         pre_s = ''
#         for s in p:
#             if pre_s + s in conn_set:
#                 pre += 1
#             else:
#                 pre = 1
#             dp_dict[s] = max(dp_dict[s], pre)
#             pre_s = s
#
#         return sum(dp_dict.values())

# 内存优化版本

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyza'
        dp_dict = {}
        conn_set = {alpha[i] + alpha[i + 1] for i in range(len(alpha) - 1)}
        pre = 0
        pre_s = ''
        for s in p:
            if pre_s + s in conn_set:
                pre += 1
            else:
                pre = 1
            dp_dict[s] = max(dp_dict.get(s, 0), pre)
            pre_s = s

        return sum(dp_dict.values())
