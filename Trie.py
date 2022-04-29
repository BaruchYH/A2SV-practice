class Trie:
    
    def __init__(self):
        self.dict = {}
        self.end = '-'

    def insert(self, word: str) -> None:
        
        temp = self.dict
        for w in word:
            if w in temp:
                temp = temp[w]
            else:
                temp[w] = {}
                temp = temp[w]
        temp[self.end] = {self.end}
        

    def search(self, word: str) -> bool:
        
        temp = self.dict
        for w in word:
            if w in temp:
                temp = temp[w]
            else:
                return False
        return self.end in temp
        

    def startsWith(self, prefix: str) -> bool:
        
        temp = self.dict
        for p in prefix:
            if p in temp:
                temp = temp[p]
            else:
                return False
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
