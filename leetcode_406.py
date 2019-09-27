class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(reverse=True, key=lambda x: (x[0], -x[1]))
        res = []
        for p in people:
            res = res[:p[1]] + [p] + res[p[1]:]
        return res
