class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
       
            a = [[0, 1], [1, 0]]   
            if n > 1:  
                v = self.kthGrammar(n-1, (k-1) // 2 + 1) 
                return a[v][(k-1)%2]
            else:
                return 0
