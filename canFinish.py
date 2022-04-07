class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        q = deque()
        graph = defaultdict(list)
        
        for pre in prerequisites:
            dst, src = pre 
            indegree[dst] += 1
            graph[src].append(dst)
            
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        cnt = 0
        while q:
            curr = q.popleft()
            cnt += 1
            for char in graph[curr]:
                indegree[char] -= 1
                if indegree[char] == 0:
                    q.append(char)
                    
        return cnt == numCourses 
        
