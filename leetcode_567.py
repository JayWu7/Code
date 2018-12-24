import profile


class Solution:
    def checkInclusion(self, s1, s2):
        """
        给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
        换句话说，第一个字符串的排列之一是第二个字符串的子串。

        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length_s1 = len(s1)
        length_s2 = len(s2)
        if length_s2 < length_s1:
            return False

        letter_dict = {}  # 用来存储s1中每个字母出现的次数
        for r in range(97, 123):
            letter_dict[chr(r)] = 0
        for letter in s1:
            letter_dict[letter] += 1
        index = 0
        length = length_s2 - length_s1

        while index <= length:  # 依次遍历s2中长度和s1一样的子串
            let_dict = letter_dict.copy()
            s = s2[index:index + length_s1]
            for l in s:  # 遍历当前判断子串的每一个字母
                if let_dict[l] > 0:  # s1有此字母且此字母剩余数量大于0
                    let_dict[l] = let_dict[l] - 1
                else:
                    index = s.index(l) + 1 + index
                    break
            else:
                return True
        else:
            return False

# excellent code
# class Solution:
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         cnt1 = [0] * 26;
#         cnt2 = [0] * 26;
#         for c in s1:
#             cnt1[ord(c) - ord('a')] += 1
#         for i in range(len(s2)):
#             cnt2[ord(s2[i]) - ord('a')] += 1
#             if i < len(s1) - 1:
#                 continue
#
#             if cnt2 == cnt1:
#                 return True
#             cnt2[ord(s2[i - len(s1) + 1]) - ord('a')] -= 1
#         return False
s = Solution()
s1 = "adc"
s2 = "dcda"
print(s.checkInclusion(s1, s2))
