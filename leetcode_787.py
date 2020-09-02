class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        current_cities = [(src, 0, K + 1)]
        costs = {u: [] for u in range(n)}
        for u, v, w in flights:
            costs.get(u, []).append((v, w))

        while current_cities:
            u, cost, k = current_cities.pop(0)
            if u == dst:
                return cost
            for v, w in costs[u]:
                if k > 0:
                    current_cities.append((v, cost + w, k - 1))

            current_cities.sort(key=lambda x: x[1])

        return -1




n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 1


S = Solution()
print(S.findCheapestPrice(n, flights, src, dst, K))
