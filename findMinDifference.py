class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def minute(time):
            H, M = time.split(':')
            
            res = int(H)*60 + int(M)
            return res 
        sorted_time = sorted([minute(tp) for tp in timePoints])
        diff = 24*60 - (sorted_time[-1] - sorted_time[0])
        n = len(timePoints)
        
        for i in range(1, n):
            if (curr := sorted_time[i] - sorted_time[i-1]) < diff: diff = curr
        return diff
