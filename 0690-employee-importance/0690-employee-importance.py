"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e_map = {}
        for emp in employees:
            e_map[emp.id] = emp

        importance = e_map[id].importance
        subord = e_map[id].subordinates
        while subord:
            next_e = e_map[subord.pop()]
            importance += next_e.importance
            subord += next_e.subordinates
        return importance