"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        nodes = {}
        processed = set()
        dq = collections.deque([node])
        while dq:
            n = dq.popleft()
            # print(n.val, n.neighbors)
            n_val, n_nb = n.val, n.neighbors

            new_nb = []
            for nb in n_nb:
                new_node = nodes.get(nb.val, Node(nb.val))
                nodes[nb.val] = new_node
                new_nb.append(new_node)
                if nb.val not in processed:
                    dq.append(nb)
                    processed.add(nb.val)

            n_node = nodes.get(n_val, Node(n_val))
            n_node.neighbors = new_nb
            nodes[n_val] = n_node
            processed.add(n_val)
        return nodes[1]
        