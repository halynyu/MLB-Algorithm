# 캠핑장
i = 1
while True:
    n = 0
    l, p, v = map(int, input().split())
    if l==0 and p == 0 and v == 0:
        break
    n += (v // p) * l
    v %= p
    if v <= l:
        n += v
    else:
        n += l
    print(f"Case {i}: {n}")
    i += 1
