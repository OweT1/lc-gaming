class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_deg = defaultdict(int)
        neighbours = defaultdict(list)

        for u, v in prerequisites:
            in_deg[v] += 1
            neighbours[u].append(v)
        
        prereq_array = [set() for i in range(numCourses)]
        dq = deque([i for i in range(numCourses) if i not in in_deg])
        while dq:
            ele = dq.popleft()
            neighbour = neighbours.get(ele, [])
            for nb in neighbour:
                in_deg[nb] -= 1
                if in_deg[nb] == 0:
                    dq.append(nb)
                # add ele and its pre-reqs to the neighbour's prereqs
                prereq_array[nb].add(ele)
                prereq_array[nb] = prereq_array[nb].union(prereq_array[ele])
        
        results = []
        for u, v in queries:
            results.append(u in prereq_array[v])
        return results