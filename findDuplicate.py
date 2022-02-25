class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1 
        right = len(nums)
        while left < right :
            count = 0
            mid = (left + right)//2
            for num in nums:
                if num <= mid :
                    count += 1
            if count > mid :
                right = mid
            else :
                left = mid + 1
        return left 
