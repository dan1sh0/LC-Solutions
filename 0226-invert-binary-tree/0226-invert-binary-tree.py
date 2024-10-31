# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # time complexity = O(n)
        if not root:
            return None 
        # create temp variable to hold the left node 
        # then swap using the temp variable
        temp = root.left 
        root.left = root.right 
        root.right = temp 
        
        # recursively call the left and right 
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root 