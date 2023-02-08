class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = []
        mapp = defaultdict(list)
        if len(adjacentPairs) == 1:
            return [adjacentPairs[0][0], adjacentPairs[0][1]]
            
        for x,y in adjacentPairs:
            mapp[x].append(y)
            mapp[y].append(x)
        for key,val in mapp.items():
            if len(val) == 1:
                res.append(key)
                res.append(val[0])
                break
        for i in range(len(adjacentPairs)-1):
            a, b = mapp[res[-1]]
            cur = a if res[-2] != a else b
            res.append(cur)
            
        return res 
