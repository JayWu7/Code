class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str 
        """

        length = len(strs)
        if not length:
            return ''
        if length is 1:
            return strs[0]

        short = min(strs, key=len)
        i = 0

        while i < length:
            if not short:
                return ''
            elif not strs[i].startswith(short):
                i = 0
                short = short[:-1]
            else:
                i = i + 1
        return short

# Others good code
# class Solution:
#     @staticmethod
#     def longestCommonPrefix( strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         res=''
#         for each in zip(*strs):
#             if len(set(each))==1:
#                 res+=each[0]
#             else:
#                 return res
#         return res
