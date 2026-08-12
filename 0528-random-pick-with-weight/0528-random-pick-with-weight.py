class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self._calc_sum()

    def _calc_sum(self):
        self.w_sum = sum(self.w)
        cumu_sum = [self.w[0]]
        for i in range(1, len(self.w)):
            cumu_sum.append(cumu_sum[-1] + self.w[i])
        self.w_cumu_sum = cumu_sum

    def pickIndex(self) -> int:
        rand_val = random.randint(1, self.w_sum)
        return bisect.bisect_left(self.w_cumu_sum, rand_val)
