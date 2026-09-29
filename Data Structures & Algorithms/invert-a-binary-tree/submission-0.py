# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using BFS -> Queue = []
# use list or deque not set(), because there is no squence in the set.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root

        q = deque()
        q.append(root)

        while q:
            node = q.popleft() # take the node out from the root 

            right = node.right 
            left = node.left 

            node.right = left
            node.left = right 
            

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root 






        