class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        target = -1
        for point in range(len(palindrome)):
            if palindrome[point] != 'a':
                target = point 
                break
        if len(palindrome)%2 == 1 and target == len(palindrome)//2 or target == -1:
            target = len(palindrome) -1
        
        def palindromeCheck(p):
            j = 0
            i = len(palindrome)-1
            while j <= i:
                if p[j] != p[i]:
                    return False
                    break 
                j += 1
                i -= 1
            return True 
        
        letters = ['a', 'b']
        idx = 0   
        if palindromeCheck(palindrome):
            for idx in range(len(letters)):
                p = palindrome[:target] + letters[idx] + palindrome[target+1:]
                if not palindromeCheck(p):
                    palindrome = p
                    break
        if len(p) == 1:
            return '' 
        else: 
            return palindrome
        
        
        
        
        
        
                
        
