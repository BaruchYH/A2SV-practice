class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        isoDic = {}
        val = ""
        for i in range(len(s)):
            if s[i] not in isoDic:
                isoDic[s[i]] = t[i] 
                if t[i] in val:
                    return False 
                val += t[i]
            elif isoDic[s[i]] != t[i]:
                return False
        return True 
                
                
            
            
            
            
#         isoDic = {}
     
#         for i in range(len(s)):
#             if s[i] not in isoDic:
#                 isoDic[s[i]] = t[i] 
#                 if t[i]+'*' in isoDic and isoDic[t[i]+'*'] == '#':
#                     return False 
#                 isoDic[t[i]+'*'] = '#'
#             elif isoDic[s[i]] != t[i]:
#                 return False
#         return True 
        
