class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #采用遗传算法解决
        """
        # 编码:自然数编码
        # 初始化染色体:
        from random import sample, randint, choice
        len_nums = len(nums)
        if len_nums == 3:
            return sum(nums)
        len_s = len_nums // 2 + 1  # 染色体数目
        codes = list()
        base_code = list(range(len_nums))
        for _ in range(len_s):
            codes.append(sample(base_code, k=3))

        # 适应性函数
        def fitness(code):
            values = [nums[i] for i in code]
            return abs(sum(values) - target)
            # 差越小，适应性越强

        # 变异函数
        def variation(code):
            i = randint(0, 2)
            while True:
                v_i = randint(0, len_nums - 1)
                if v_i not in code:
                    break
            code[i] = v_i

        # 选一个出，挑一个进

        # 交叉函数
        def mul_parents(fa, mo):
            f = fa.copy()
            m = mo.copy()

            n1 = randint(0, 2)
            while True:
                n2 = randint(0, 2)
                if abs(n1 - n2) != 2:
                    break

            if n1 > n2: n1, n2 = n2, n1

            while n1 <= n2:
                t1 = f[n1]
                t2 = f[n2]
                if t1 not in m: m[n2] = t1
                if t2 not in f: f[n1] = t2
                n1 += 1

            son = f if fitness(f) < fitness(m) else m
            return son

        # 选择函数
        def select():
            nonlocal codes
            codes.sort(key=lambda co: fitness(co))
            len_s = len(codes)
            new_codes = []

            se_num = len_s // 2

            # 随机挑选父代，交叉生成子代
            for _ in range(se_num):
                fa, mo = sample(codes, k=2)

                son = mul_parents(fa, mo)
                new_codes.append(son)

            # 每次挑两个，添加ftness小的那个，挑len_s - se_num - 1个

            for _ in range(len_s - se_num - 1):
                s1, s2 = sample(codes[1:], k=2)
                s = s1 if fitness(s1) < fitness(s2) else s2
                new_codes.append(s)

            # 变异：  概率=0.
            va_num = int(len_s * 0.4)
            for _ in range(va_num):
                v_s = choice(new_codes)
                variation(v_s)

            # 精英选择
            new_codes.append(codes[0])
            codes = new_codes

        # 200次进化
        for _ in range(140):
            select()

        code = codes[-1]
        res = [nums[i] for i in code]
        return sum(res)


s = Solution()

print(s.threeSumClosest([-43,61,-62,24,73,64,-23,94,-65,-27,24,-56,8,54,0,19,-100,-64,-53,6,-22,13,-18,55,-41,37,34,-43,0,-8,-95,76,73,21,-93,16,98,60,70,-32,30,-7,-27,-73,79,-26,41,32,41,-5,82,-14,50,-94,22,62,60,-48,51,12,-34,68,-40,-20,-20,46,46,-79,1,82,-98,41,-79,-43,-76,-25,-94,-16,-25,46,-95,-79,53,-1,-30,43,93,17,72,66,83,-89,-16,42,40,87,-46,40,22,85,-91,46,-77,19,-56,-28,8,47,-20,65,8,60,-49,-86,-74,56,30,79,97,-89,14,-90,66,-12,-57,46,-61,87,72,13,75,75,36,79,-16,84,-49,-86,76,68,-8,-65,-86,-11,55,-69,-59,34,63,59,-11,43,16,7,93,57,-55,2,38,64,3,22,-9,-22,-34,-84,90,-71,-88,64,-19,13,-8,-81,-95,-38,-9,-25,82,57,60,-26,66,21,8,65,-38,-68,-59,24,91],-231))