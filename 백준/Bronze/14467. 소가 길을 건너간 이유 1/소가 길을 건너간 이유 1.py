n = int(input())
d = dict()
count = 0

for _ in range(n):
    cow, location = map(int, input().split())
    if cow not in d:
        d[cow] = location
    else:
        if d[cow] != location:
            count += 1
            d[cow] = location

print(count)