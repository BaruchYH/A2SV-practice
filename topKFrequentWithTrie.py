class Try:
    def __init__(self):
        self.alphabet = [None]*26
        self.word = ''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        wordFreq = collections.Counter(words)
        bucket = [None]*(len(words)+1)
        
        for word, freq in wordFreq.items():
            if not bucket[freq]:
                bucket[freq] = Try()
            self.addWord(bucket[freq], word)
            
        ans = []
        i = len(words) - 1
        while i >= 1 and len(ans) < k:
            if bucket[i]:
                self.getWord(bucket[i], ans, k)
            i -= 1
        return ans
    def addWord(self, root, word):
        
        node = root
        for w in word:
            idx = ord(w)-ord('a')
            if not node.alphabet[idx]:
                node.alphabet[idx] = Try()
            node = node.alphabet[idx]
        node.word = word
        
    def getWord(self, node, ans, k):
        if not node: return 
        if node.word:
            ans.append(node.word)
        if len(ans) == k: return 
        for val in node.alphabet:
            self.getWord(val, ans, k)
        
            
        
        
