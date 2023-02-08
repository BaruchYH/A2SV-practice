class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for idx in range(len(equations)):
            graph[equations[idx][0]][equations[idx][1]] = values[idx]
            graph[equations[idx][1]][equations[idx][0]] = 1/values[idx]
            
        def dfs(a,b,visited):
            if not a in graph or not b in graph:
                return -1.0
            
            if b in graph[a]:
                return graph[a][b]
            
            
            for x in graph[a]:
                if x not in visited:
                    visited.add(x)
                    temp = dfs(x,b,visited)
                    if temp == -1:
                        continue 
                    else:
                        return temp*graph[a][x]
                    
            return -1 
                        
                
                 
        ans = []
        for q in queries:
            ans.append(dfs(q[0], q[1],set()))
            
        return ans 
        
