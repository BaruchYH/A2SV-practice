class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email = {i:i for i in range(len(accounts))}
        
        def find(x):
            if email[x] != x:
                email[x] = find(email[x])
            return email[x]
                
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            email[rootx] = rooty
                
        for i, accounts_i in enumerate(accounts):
            for j, accounts_j in enumerate(accounts[:i]):
                if accounts_i[0] == accounts_j[0]:
                    records = set(accounts_i[1:])
                    for eml in accounts_j[1:]:
                        if eml in records:
                            union(i, j)
                            break
                            
        merged = [set() for i in range(len(accounts))]
        for k, emails in enumerate(accounts):
            for em in emails[1:]:
                merged[find(email[k])].add(em)
            
        ans = []
        for l, elements in enumerate(merged):
            if elements:
                ans.append([accounts[l][0]]+sorted(list(elements)))
            
            
        return ans 
            
         
            
                
                
        
