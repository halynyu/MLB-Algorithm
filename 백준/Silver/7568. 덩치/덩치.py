n = int(input())

arr = []
for _ in range(n):
    weight, height = map(int, input().split())
    arr.append((weight, height))

rate = [1] * len(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            rate[i] += 1

print(*rate)