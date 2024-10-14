n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    inc = 1
    dec = 1
    max_len = 1
    
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc += 1
            dec = 1
        elif arr[i] < arr[i-1]:
            dec += 1
            inc = 1
        else:
            inc += 1
            dec += 1
        
        max_len = max(max_len, inc, dec)
        
    print(max_len)
        

        
        