class Solution:
    def lengthOfLongestSubstring(self, s):
        str_dict = {}
        i = 0
        le = ''
        st = ''
        if s=='':
            return 0
        else:
            while True:
                le = s[i]
                if le in st:
                    str_dict.setdefault(st, st.__len__())
                    st = s[s.index(le) + 1:i + 1]
                    i -= s.index(le)
                    s = s[s.index(le) + 1:]
                else:
                    st += le
                    i += 1
                if (i >= s.__len__()):
                    str_dict.setdefault(st, st.__len__())
                    break

            return max(str_dict.values())
