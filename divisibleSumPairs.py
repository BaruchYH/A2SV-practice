def divisibleSumPairs(n, k, ar):
    # Write your code here
    count1 = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k == 0:
                count1 += 1
    return count1
