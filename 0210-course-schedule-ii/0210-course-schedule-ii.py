class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_deg = {i: 0 for i in range(numCourses)}
        neighbours = defaultdict(list)
        for pr in prerequisites:
            neighbours[pr[1]].append(pr[0])
            in_deg[pr[0]] += 1

        pq = [k for k, v in in_deg.items() if v == 0]
        res = []
        while pq:
            ele = pq.pop()
            res.append(ele)
            if ele in neighbours:
                nb = neighbours[ele]
                for n in nb:
                    in_deg[n] -= 1
                    if in_deg[n] == 0:
                        pq.append(n)
        return res if len(res) == numCourses else []
