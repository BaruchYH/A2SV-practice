def repeatedString(s, n): 
    count1 = 0
    count2 = 0
    count3 = 0
    if len(s) < n :
        if n%len(s) == 0:
            for h in s:
                if h == 'a':
                    count1 += 1
            ans = int((n/len(s))*count1)
            
        elif n%len(s) != 0:
            for r in s:
                if r == 'a':
                    count2 += 1
            dif = n - int(n/len(s))*len(s)
            for i in range(0, dif):
                if s[i] == 'a' :
                    count3 += 1
            ans = int((int(n/len(s)))*count2 + count3)         
    if len(s) > n:
        for i in range(0,n):
            if s[i] == 'a':
                count1 += 1
        ans = count1 
    return int(ans) 
