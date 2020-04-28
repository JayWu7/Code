class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 设置最大、二大、三大变量
        fm = sm = tm = -float('inf')
        for n in nums:
            if n >= fm:
                if n != fm:
                    fm, sm, tm = n, fm, sm
            elif n >= sm:
                if n != sm:
                    sm, tm = n, sm
            elif n >= tm:
                if n != tm:
                    tm = n

        return tm if tm > -float('inf') else fm
                   