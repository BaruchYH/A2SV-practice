    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0] 
        i = 0
        temp = ""
        
        while i < len(strs):
            for j in range(min( len(s), len(strs[i]))):
                if s[j] != strs[i][j]:
                    break
                temp += s[j]
            if temp == "":
                return ""
            s = temp 
            temp = ""
            i += 1
                           
        return s 
        
                
