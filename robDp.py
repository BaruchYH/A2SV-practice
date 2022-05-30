class Solution:
    def rob(self, nums: List[int]) -> int:
        def find(i, nums, dp):

            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(find(i+2, nums, dp), find(i+3, nums, dp)) + nums[i]
            return dp[i]
        
        dp = [-1]*len(nums)
        return max(find(0, nums, dp), find(1, nums, dp))
