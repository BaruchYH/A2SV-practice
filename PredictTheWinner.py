class Solution:
    
    def PredictTheWinner(self, nums: List[int]) -> bool: 
        
        def Predict(s, e):
         
            if s == e :
                return nums[s]
           
            else :
                return max(nums[s] - Predict(s+1, e) , nums[e] - Predict(s, e-1))
            
        return Predict(0, len(nums)-1 ) >= 0
