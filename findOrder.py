class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0]*numCourses 
        q = deque()
        for pre in prerequisites:
            dst, src = pre
            indegree[dst] += 1
            graph[src].append(dst)
                        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        cnt = 0
        li = []
        while q:
            curr = q.popleft()
            li.append(curr)
            cnt += 1
            for char in graph[curr]:
                indegree[char] -= 1
                if indegree[char] == 0:
                    q.append(char)
                
        if cnt == numCourses:
            return li
        else:
            return []
            
            
        
