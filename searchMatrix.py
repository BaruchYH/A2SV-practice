class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) 
        for i in range(m):
            left = 0
            right = n-1
            if matrix[i][n-1] < target:
                continue 
            while left <= right:
                mid = (left+right)//2
                if matrix[i][mid] == target:
                    return True 
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return False 
