# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(low, high, value):
            if value is None:
                return True
            if value.val <= low or value.val >= high:
                return False
            
            return dfs(low, value.val, value.left) and dfs(value.val, high, value.right)
        
        return dfs(float('-inf'), float('inf'), root)
