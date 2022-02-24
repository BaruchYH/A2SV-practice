class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else :
                dict[word] = 1
        heap = []
        result = []
        for keys,friqword in dict.items():
            heapq.heappush(heap,(-friqword,keys))
        for _ in range(k):
            wordtouple = heapq.heappop(heap)
            result.append(wordtouple[1])
        
        return result 
            
                
            
        
