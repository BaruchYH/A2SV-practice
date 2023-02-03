class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                first_palindrome = s[l + 1: r + 1]
                second_palindrome = s[l: r]
                if first_palindrome == first_palindrome[:: -1] or second_palindrome == second_palindrome[:: -1]: return True
                else: return False
        return True
        
