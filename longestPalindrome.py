class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = (0, 0)
        for i in range(len(s)):
            odd = self.isPalindrome(i, i, s)
            if ans[1]-ans[0] < odd[1]-odd[0]:
                ans = odd
            even = self.isPalindrome(i, i+1, s)
            if ans[1]-ans[0] < even[1]-even[0]:
                ans = even
        return s[ans[0]:ans[1]]
            
        
    def isPalindrome(self, l, r, str_):
        
        
        while l >= 0 and r < len(str_) and str_[l] == str_[r]:
            l -= 1
            r += 1
            
        return (l+1, r)

            
         
