import sys
input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    list.append(int(input()))
    
for i in sorted(list):
    print(i)