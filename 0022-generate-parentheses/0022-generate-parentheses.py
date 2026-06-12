class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(c: str, num_left: int, num_right: int):
            if num_left == num_right == 0:
                res.append(c)
                return
            elif num_left == 0:
                res.append(c + num_right * ")")
                return

            if num_left == num_right:
                dfs(c+"(", num_left-1, num_right)
            else:
                dfs(c+"(", num_left-1, num_right)
                dfs(c+")", num_left, num_right-1)
        dfs("", n, n)
        return res

        