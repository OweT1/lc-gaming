class Solution:
    def decodeString(self, s: str) -> str:
        curr_multiplier = ""
        multiplier = []
        store = []
        for c in s:
            if c.isnumeric():
                curr_multiplier += c
            elif c == "[":
                multiplier.append(int(curr_multiplier))
                curr_multiplier = ""
                store.append(c)
            elif c == "]":
                tmp = []
                while store:
                    ele = store.pop()
                    if ele == "[":
                        store.append("".join(tmp[::-1]) * multiplier.pop())
                        break
                    else:
                        tmp.append(ele)
            else:
                store.append(c)
        return "".join(store)
        