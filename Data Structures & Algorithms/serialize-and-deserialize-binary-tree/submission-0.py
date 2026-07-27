# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""
        queue = deque()
        queue.append(root)
        #print("result = ", result)
        #print("queue = ",   queue)

        def dfs(root):
            if not root:
                return "None#"
            return str(root.val)+"#"+ dfs(root.left) + dfs(root.right)

        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        d = data.split("#")
        di = [0]
        def dfs():
            if d[di[0]] == "None":
                di[0] +=1
                return None
            node = TreeNode(int(d [di[0]]))
            di[0] +=1
            node.left = dfs()
            node.right = dfs()
            return node 
        return dfs()