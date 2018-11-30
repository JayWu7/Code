class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s,[],res)
        return res

    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:  # 剩余部分太长
            return

        if not s and len(path) == 4:
            res.append('.'.join(path))  # 合法ip

        for index in range(min(3, len(s))):
            cur_path = s[:index + 1]
            if cur_path[0] == '0' and len(cur_path) > 1 or int(cur_path) > 255:
                continue
            self.dfs(s[index + 1:], path + [cur_path], res)

s =Solution()
print(s.restoreIpAddresses('25525511135'))