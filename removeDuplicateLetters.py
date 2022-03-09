class Solution:
    from collections import Counter 
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        countOfLetters = Counter(s)
        for i in s:
            countOfLetters[i] -=1
            if i in stack:
                continue 
            while stack and stack[-1] > i and countOfLetters[stack[-1]]:
                stack.pop()
            stack.append(i)        
        return "".join(stack)
