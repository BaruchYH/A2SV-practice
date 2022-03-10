class Solution:
    def fib(self, n: int) -> int:
        li = [0]*n
        if n == 0:
            return 0
        if n == 1:
            return 1
        li[0] = 1
        li[1] = 1
        for i in range(2,n):
            li[i] = li[i-1] + li[i-2]
        return li[n-1]
