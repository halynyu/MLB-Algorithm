import sys
input = sys.stdin.readline

n = int(input())
human_list = list(map(int, input().split()))

human_list.sort()

answer = []
answer.append(human_list[0])

for i in range(1, n):
    answer.append(answer[-1] + human_list[i])

print(sum(answer))