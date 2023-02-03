# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root,r,c):
            if not root: return 
            store[r].append((c, root.val))
            dfs(root.left,r-1,c+1)
            dfs(root.right,r+1,c+1)
        store = defaultdict(list)
        dfs(root,0,0)            
        return [ [t for n,t in sorted(val)] for key, val in sorted(store.items())]
