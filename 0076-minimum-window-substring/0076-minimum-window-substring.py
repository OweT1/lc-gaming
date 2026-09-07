class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        sliding_counter = {}
        l = r = 0
        res = None

        while r < len(s):
            print('start', l, r)
            c = s[r]
            if c not in sliding_counter:
                sliding_counter[c] = 0
            sliding_counter[c] += 1

            contains = True
            for k, v in t_counter.items():
                if sliding_counter.get(k, 0) < v:
                    contains = False
                    break

            if contains:
                while l < r:
                    if s[l] not in t_counter or (s[l] in t_counter and sliding_counter[s[l]] > t_counter[s[l]]):
                        sliding_counter[s[l]] -= 1
                        if sliding_counter[s[l]] == 0:
                            sliding_counter.pop(s[l])
                        l += 1
                    else:
                        break

                if res is None or r - l < len(res):
                    res = s[l:r+1]
            
            r += 1
        return res if res is not None else ""