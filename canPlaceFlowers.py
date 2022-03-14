class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: 
        idx = 0
        cnt = 0
        while idx < len(flowerbed):
            if cnt == n:
                return True 
            if idx == len(flowerbed)-1 and not flowerbed[idx]:
                cnt += 1
                idx += 1
                continue 
            if flowerbed[idx]:
                idx += 2
                continue 
            if not flowerbed[idx] and not flowerbed[idx+1]:
                flowerbed[idx] == 1
                cnt += 1
                idx += 2
                continue 
            idx += 1
            
        return cnt >= n 
                
                
