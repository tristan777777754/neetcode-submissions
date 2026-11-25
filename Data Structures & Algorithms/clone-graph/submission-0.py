"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        record = {}

        def dfs(node):

            if node in record:
                return record[node]
            
            copy = Node(node.val)

            record[node] = copy 

            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        if node is None:
            return None
        
        return dfs(node)
      

