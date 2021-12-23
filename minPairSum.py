class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minPairSum = 0
        for i in range(0, int( len(nums)/2 ) + 1 ):
             minPairSum = max( nums[0+i]+nums[int(len(nums)-1)-i] , minPairSum )
        return minPairSum
