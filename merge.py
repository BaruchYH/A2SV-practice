class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        li = []
        isTrue = True 
        count = 0
        while isTrue :
                for i in range(1, len(intervals)):
                    if intervals[i-1][1] > intervals[i][0]:
                        li.append([intervals[i-1][0], intervals[i][1]])
                        count += 1
                    else :
                        li.extend(intervals[i-1])
                        li.extend(intervals[i])
                intervals.append(li)
                print()
                if count > 0 :
                    isTrue = True
                else :
                    isTrue = False
                count = 0 
        return intervals 
