class Solution:
    def findJudge(self, N: int, trust: list[list[int]]) -> int:
        judge_dict = {}
        not_judge = set()
        for item in trust:
            not_judge.add(item[0])
            if item[0] in judge_dict:
                judge_dict.pop(item[0])

            if item[1] in not_judge:
                continue
            elif item[1] in judge_dict:
                judge_dict[item[1]].add(item[0])
            else:
                judge_dict[item[1]] = {item[0]}

        if judge_dict:
            res = judge_dict.popitem()
            if len(res[1]) == N - 1:
                return res[0]
        elif N == 1:
            return 1

        return -1
