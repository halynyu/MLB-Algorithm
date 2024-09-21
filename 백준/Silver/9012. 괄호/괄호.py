n = int(input())

for _ in range(n):
    arr = list(input())
    while len(arr) != 0:
        if arr[0] == ')':
            print('NO')
            break
        else:
            if ')' in arr:
                arr.remove('(')
                arr.remove(')')
            else:
                print('NO')
                break
    if len(arr) == 0:
        print('YES')