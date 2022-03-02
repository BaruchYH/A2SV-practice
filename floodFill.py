class Solution: 
    
    def flood(self , image , x , row_x , y , col_y , newColor , oldColor):
        if 0<= x < row_x and 0 <= y < col_y and image[x][y] == oldColor :
            image[x][y] = newColor
            self.flood(image , x-1 , row_x , y , col_y , newColor , oldColor)
            self.flood(image , x+1 , row_x , y , col_y , newColor , oldColor)
            self.flood(image , x , row_x , y-1 , col_y , newColor , oldColor)
            self.flood(image , x , row_x , y+1 , col_y , newColor , oldColor)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        row_x = len(image)
        col_y = len(image[0])
        x = sr
        y = sc
        if oldColor != newColor:
            self.flood(image , x , row_x , y , col_y , newColor , oldColor)
        return image 
            
        
