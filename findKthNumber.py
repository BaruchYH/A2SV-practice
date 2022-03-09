lass Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
       
        def kthSmallest(mid):
            count = 0
            for i in range(1,m+1):
                count += min(n, mid//i)
            return count 
        
        left = 0
        right = m*n 
        while left < right:
            mid = (left + right)//2
            if kthSmallest(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return right 
                
