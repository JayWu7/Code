class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l_path = path.split('/')
        list_path = [l for l in l_path if l != '']
        simplified_path = list()

        for path in list_path:
            if path == '.':
                continue
            elif path == '..':
                if simplified_path:
                    simplified_path.pop()
                else:
                    simplified_path = simplified_path[:-1]
            else:
                simplified_path.append(path)
        else:
            path = '/' + '/'.join(simplified_path)
            return path


s = Solution()
print(s.simplifyPath(""))
