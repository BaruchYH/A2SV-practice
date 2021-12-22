def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        arrCount = dict(Counter(arr))
        x = sorted(arrCount.values())
        y = 0
        counter = 0
        for i in range(0,len(x)): 
            y += x.pop()
            counter += 1
            if y >= len(arr)/2 :
                break
        return counter
