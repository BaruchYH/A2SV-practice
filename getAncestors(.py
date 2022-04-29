class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adj_list = defaultdict(list)
        for x1, x2 in edges:
            adj_list[x2].append(x1)
        
        ans = []
        memo = {}
        for i in range(n):
            ans.append(sorted(self.dfs(adj_list, i, memo)))
            
        return ans 
    
        
    def dfs(self, graph, node, memo):
        if len(graph[node]) == 0:
            return []
        if node not in memo:
            memo[node] = set()
            for child in graph[node]:
                memo[node].update(self.dfs(graph, child, memo))
                memo[node].add(child)
                
        return memo[node]

                

                
            
            
        
