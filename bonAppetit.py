def bonAppetit(bill, k, b):
    # Write your code here
    bill.pop(k)
    Sum = sum(bill)/2
    if Sum == b :
        return print('Bon Appetit')
    elif b > Sum:
        return print(int(b - Sum))
