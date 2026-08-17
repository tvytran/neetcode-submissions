# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []
        curr = []
        t = 1
        count = 0
        while queue:
            target = queue.popleft()
            count += 1
            if target.left:
                queue.append(target.left)
            if target.right:
                queue.append(target.right)

            curr.append(target.val)
            if t == count:
                #print("h")
                count = 0 
                t = len(queue)
                result.append(curr)
                curr = []
        if len(curr) > 0:
            result.append(curr)
        
        return result
            
        