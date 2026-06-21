class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cost_index = [0 for _ in range(max(costs)+1)]

        for c in costs:
            cost_index[c] += 1

        res = 0
        for i, c in enumerate(cost_index):
            for _ in range(c):
                if coins >= i:
                    res += 1
                    coins -= i
                else:
                    break
        return res
