class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        while left <= right :
            midpoint = (left+right)//2
            if nums[midpoint] == target :
                while nums[left] != target or nums[right] != target :  
                    right -= 1
                return [left,right]
            elif nums[midpoint] > target :
                right = midpoint - 1
            elif nums[midpoint] < target :
                left = midpoint + 1
        return [-1,-1]
                    
                    
                    
        
