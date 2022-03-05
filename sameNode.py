class Solution: 
    def sameNode(self, l, r):
        if not l and not r:
            return True 
        elif not l or not r:
            return False 
        elif l.val != r.val:
            return False
        return self.sameNode(l.left,r.right) and self.sameNode(l.right,r.left)
                                
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.sameNode(root,root)
