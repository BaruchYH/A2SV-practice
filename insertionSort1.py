def print_arr(arr):
    for i in arr:
        print(i, end = " ")
    print("\n", end = "")

def insertionSort1(n, arr):
    # Write your code here
    x = arr[n-1]
    for i in range(1,n):     
        if arr[n-i-1] > x :
            arr[n-i] = arr[n-i-1]
            print_arr(arr)   
        else :
            arr[n-i] = x 
            print_arr(arr)
            break 
        
    if arr[0] > x :
            arr[0] = x
            print_arr(arr)
