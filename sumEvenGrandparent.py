class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def grandParent(granpa, parent, node):
            
            if granpa and granpa.val%2 == 0:
                yield node.val   
            if node.left:
                yield from grandParent(parent, node, node.left)
            if node.right:
                yield from grandParent(parent, node, node.right) 
           
        return sum(grandParent(None, None, root))  
