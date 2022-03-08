
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lev = []
        def average(node,level):
            if not node:
                return 
            if level < len(lev):
                lev[level].append(node.val)
            if level >= len(lev):
                lev.append([node.val])
            average(node.left, level+1)
            average(node.right, level+1)
        average(root, 0)
        
        li = []
        for i in range(len(lev)):
            x = sum(lev[i])
            y = len(lev[i])
            li.append(x/y)         
            
        return li
