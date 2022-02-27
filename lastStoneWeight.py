class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for _ in stones:
            heapq.heappush(hp,-_)
        while len(hp) > 1:
            x = heapq.heappop(hp)
            y = heapq.heappop(hp)
            x = x-y
            if x:
                heapq.heappush(hp,x)
                
        return 0 if len(hp) == 0 else -hp[0]
                
        
