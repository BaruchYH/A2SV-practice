class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        _range = right - left 
        mask = 0XFFFFFFFF
        
        while _range :
#             what is this masking doing ??
            mask &= mask-1  
            _range = _range >> 1
            
        return left & right & (mask)
        
