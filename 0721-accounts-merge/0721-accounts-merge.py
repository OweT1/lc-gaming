class UF:
    def __init__(self, length: int):
        self.length = length
        self.parent = list(range(length))
        self.size = [1] * length
    
    def find(self, e: int):
        while e != self.parent[e]:
            e = self.parent[e]
        return e
    
    def union(self, e1: int, e2: int):
        p1, p2 = self.find(e1), self.find(e2)
        if p1 == p2: return

        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        emailToAccMap = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in emailToAccMap:
                    emailToAccMap[email] = i
                else:
                    uf.union(emailToAccMap[email], i)
        
        groups = {}
        for e, i in emailToAccMap.items():
            root = uf.find(i)

            if root not in groups:
                groups[root] = []
            
            groups[root].append(e)
        
        res = []
        for r, e in groups.items():
            res.append([accounts[r][0]] + sorted(e))
        return res
        


    
        