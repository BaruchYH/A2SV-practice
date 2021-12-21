    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sub = []
        li = []
        for j in range(0, len(l)) :
                li.extend(list(nums[l[j]:r[j]+1]))
                li.sort()
                d = li[1] - li[0]
                for i in range(0,  r[j] - l[j]) :
                        if li[i+1] - li[i] != d:
                            sub.append(False)
                            break
                        elif i + 1 == r[j] - l[j] :
                                sub.append(True)
                         
                li.clear()
                
        return sub 
