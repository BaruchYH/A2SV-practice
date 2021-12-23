class Solution:
    def isValid(self, s: str) -> bool:
        li = []   
        for c in s :
            if c in ['(', '{', '[']:
                li.append(c)
            elif c == ')' and len(li) != 0 and li[-1] == '(':
                 li.pop()
            elif c == '}' and len(li) != 0 and li[-1] == '{':
                 li.pop()
            elif c == ']' and len(li) != 0 and li[-1] == '[':
                 li.pop()
            else :
                return False 
        return li == []
