class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        mask = 1
        ans = 0
        for i in range(32):
            cnt = 0
            
            for num in nums:
                temp = mask & num
                if temp:
                    cnt += 1
            if cnt % 3:
                ans = ans | mask
            mask = mask << 1
            
            
        if ans >= 2**31:
            ans -= 2**32
            
        return ans 
                
