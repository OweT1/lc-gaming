class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        temp = ""
        
        def backtrack(i: int):
            nonlocal res, temp
            if i == len(digits):
                res.append(temp)
                return

            digit = digits[i]
            characters = numpad_mapping[digit]
            for c in characters:
                temp += c
                backtrack(i+1)
                temp = temp[:-1]

        backtrack(0)
        return res