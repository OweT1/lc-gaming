class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbours = defaultdict(list)
        in_deg = defaultdict(int)

        for prereq in prerequisites:
            u, v = prereq
            in_deg[v] += 1
            neighbours[u].append(v)
        
        dq = deque([i for i in range(numCourses) if i not in in_deg])
        coursesTaken = 0
        while dq:
            ele = dq.popleft()
            ele_nb = neighbours.get(ele, [])
            for nb in ele_nb:
                in_deg[nb] -= 1
                if in_deg[nb] == 0:
                    dq.append(nb)
            coursesTaken += 1
        return coursesTaken == numCourses
        