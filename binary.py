# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)    # Go Left
            res.append(node.val)  # Visit Root
            inorder(node.right)   # Go Right
            
        inorder(root)
        return res
