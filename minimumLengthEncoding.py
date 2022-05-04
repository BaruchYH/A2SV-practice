class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        root_node = dict()
        unique_node = set(words)
        isLeafNode = lambda node: len(node) == 0
        tail_nodes = []
        
        for word in unique_node:
            
            curr = root_node
            
            for letter in reversed(word):
                curr[letter] = curr.get(letter, dict())
                curr = curr[letter]
                
            tail_nodes.append((curr, len(word)+1))
            
        return sum(suffix_len for node, suffix_len in tail_nodes if isLeafNode(node))
            
         
        
        
