import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    x = list(input().split())
    a = x[0]

    if a == 'add':
        if int(x[1]) not in arr:
            arr.append(int(x[1]))

    elif a == 'remove':
        if int(x[1]) in arr:
            arr.remove(int(x[1]))

    elif a == 'check':
        if int(x[1]) in arr:
            print(1)
        else:
            print(0)

    elif a == 'toggle':
        if int(x[1]) in arr:
            arr.remove(int(x[1]))
        else:
            arr.append(int(x[1]))
    
    elif a == 'all':
        arr = [i for i in range(1, 21)]
    
    elif a == 'empty':
        arr.clear()