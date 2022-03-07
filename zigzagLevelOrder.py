 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zig = []
        def traversZigZag(root,level):
            if not root:
                return 
            if level < len(zig):
                zig[level].append(root.val)
            if level >= len(zig):
                zig.append([root.val])
            level += 1
            traversZigZag(root.left,level)
            traversZigZag(root.right, level)
        traversZigZag(root, 0)
        
        for i in range(len(zig)):
            if i%2 == 1:
                zig[i].reverse() 
                
        return zig 
            
        
