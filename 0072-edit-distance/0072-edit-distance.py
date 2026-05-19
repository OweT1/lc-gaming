class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        distance_mapping = []
        distance_mapping.append([i for i in range(len(word1)+1)])
        for i in range(1, len(word2)+1):
            distance_mapping.append([i] + [-1 for _ in range(len(word1))])

        # define key logic
        def helper(i: int, j: int) -> int:
            if distance_mapping[j][i] != -1: # if it exists and is valid, return
                return distance_mapping[j][i]
 
            if word1[i-1] == word2[j-1]:
                distance_mapping[j][i] = helper(i-1, j-1)
                return distance_mapping[j][i]
            else:
                distance_mapping[j][i] = 1 + min(
                    helper(i-1, j-1),
                    helper(i, j-1),
                    helper(i-1, j)
                )
                return distance_mapping[j][i]
        return helper(len(word1), len(word2))