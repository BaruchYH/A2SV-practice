class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        stack1 = []
        x = ""
        
        for i in s:
            if i == ')':
                
                while stack[-1] != '(':
                        stack1.append(stack.pop()) 
                        
                stack.pop()
                stack.extend(stack1)
                stack1 = []
                
            else :
                stack.append(i)
                
        for i in stack :
             x += i
                
        return x
                
