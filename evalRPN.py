class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  
        for i in tokens:
            if i not in ['*', '/', '+', '-']:
                stack.append(int(i))
            else :   
                save = stack.pop()
                result = stack.pop()
                if i == '+' :
                    result = result + save
                if i == '*' :
                    result = result * save
                if i == '/' :
                    result = int(result / save)
                if i == '-' :
                    result = result - save
                stack.append(result)
               
        return stack.pop()
