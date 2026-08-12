class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self._calc_sum()

    def _calc_sum(self):
        self.w_sum = sum(self.w)
        cumu_sum = [0, self.w[0]]
        for i in range(1, len(self.w)):
            cumu_sum.append(cumu_sum[-1] + self.w[i])
        self.w_cumu_sum = cumu_sum

    def binary_search(self, v: int):
        l, r = 0, len(self.w_cumu_sum) - 1
        m = (l + r) // 2
        change = True
        while change:
            change = False
            if v == self.w_cumu_sum[m]:
                print(m)
                return m
            elif v > self.w_cumu_sum[m]:
                change = l != m
                l = m
                m = (l + r) // 2
            else:
                change = r != m
                r = m
                m = (l + r) // 2
        return m

    def pickIndex(self) -> int:
        rand_val = random.randint(0, self.w_sum-1)
        return self.binary_search(rand_val)
