class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        j = len(nums)-1
        while i <= j:
            r = nums[j]**2
            l = nums[i]**2
            if  r <= l:
                ans.append(l)
                i+=1             
            else:
                ans.append(r)
                j-=1
                
        
        return ans[::-1]
