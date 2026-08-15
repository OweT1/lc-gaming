class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        edge_dict = defaultdict(list)
        
        for i, origin in enumerate(bombs):
            for j, dest in enumerate(bombs):
                if i != j:  
                    if math.pow(dest[0] - origin[0], 2) + math.pow(dest[1] - origin[1], 2) <= math.pow(origin[2], 2):
                        edge_dict[i].append(j)
        
        max_bombs = 0
        for i, bomb in enumerate(bombs):
            explode_bombs = [(i, bomb)]
            visited = [0]*len(bombs)
            visited[i] = 1

            while explode_bombs:
                b, to_explode = explode_bombs.pop()
                bombs_in_range = edge_dict[b]
                for j in bombs_in_range:
                    if not visited[j]:
                        visited[j] = 1
                        explode_bombs.append((j, bombs[j]))
            
            max_bombs = max(max_bombs, sum(visited))
        return max_bombs
                    




