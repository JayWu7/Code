class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for l in magazine:
            if l in mag_dict:
                mag_dict[l] = mag_dict[l] + 1
            else:
                mag_dict[l] = 1

        for s in ransomNote:
            if s in mag_dict and mag_dict[s] > 0:
                mag_dict[s] = mag_dict[s] - 1
            else:
                return False
        return True


# method2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for a in ransomNote:
            if a in magazine:
                magazine = magazine.replace(a, '', 1)
            else:
                return False
        return True


#method 3    使用内置的all()函数
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = [magazine.count(i) >= ransomNote.count(i) for i in set(ransomNote)]
        return all(res)
