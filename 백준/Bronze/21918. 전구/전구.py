n, m = map(int, input().split())
s = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        s[b-1] = c
    elif a == 2:
        for i in range(b, c+1):
            s[i-1] = 1 - s[i-1]  # 0은 1로, 1은 0으로
    elif a == 3:
        for i in range(b, c+1):
            s[i-1] = 0
    else:
        for i in range(b, c+1):
            s[i-1] = 1

print(*s)
