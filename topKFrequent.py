class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums :
            if num in dict :
                dict[num] += 1
            else :
                dict[num] = 1
                
        heap = []
        result = []
        for keys , friq in dict.items():
            heapq.heappush(heap,(-friq,keys))    
        for _ in range(k):
            touple = heapq.heappop(heap)
            result.append(touple[1])
            
        return result 
