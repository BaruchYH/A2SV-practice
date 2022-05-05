class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
    
class Try:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        
        temp = self.root
        for w in word:
            if w not in temp.children:
                temp.children[w] = TrieNode()
            temp = temp.children[w]
        temp.end = True
        
    def findTheLongestWord(self):
        
        def helper(node, partial_ans):
            
            ans_b = partial_ans
            for c, child in node.children.items():
                if child.end:
                    ans_a = helper(child, partial_ans+c)
                    if len(ans_a) > len(ans_b):
                        ans_b = ans_a
                    elif len(ans_b) == len(ans_a) and ans_a < ans_b:
                        ans_b = ans_a

            return ans_b
                
                
                
        
        return helper(self.root, '')

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        T = Try()
        for word in words:
            T.insert(word)
        return T.findTheLongestWord()
        
        
        
