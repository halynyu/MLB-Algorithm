list = []

for _ in range(10):
    x = int(input())
    list.append(x % 42)

print(len(set(list)))