class Solution:
    def romanToInt(self, s):

        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        specials = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        number = 0
        index = 0

        while index < len(s):
            sp = s[index:index + 2]
            if sp in specials: 
                number += specials[sp]
                index += 2
            else:
                number += values[s[index]]
                index += 1


        return number

# excellent code
# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         h = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         r, p = 0, 'I'
#         for c in s[::-1]:
#             r, p = r + h[c] if h[c] >= h[p] else r - h[c], c
#         return r
