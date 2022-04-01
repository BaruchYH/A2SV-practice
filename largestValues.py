class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        que.append(root)
        ans = []
        if not root :
            return []
        while que:
            n = len(que)
            currMax = -float(inf)
            
            while n:
                curr = que.popleft()
                currMax = max(curr.val, currMax)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                n -= 1
            ans.append(currMax)
                
            
        return ans 
