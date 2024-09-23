import sys
input = sys.stdin.readline

n = int(input())

stair_list = []
for _ in range(n):
    stair_list.append(int(input()))

dp_list = [0] * n

if n <= 2:
    print(sum(stair_list))
else:
    dp_list[0] = stair_list[0]
    dp_list[1] = stair_list[0] + stair_list[1]

    for i in range(2, n):
        dp_list[i] = max(dp_list[i - 3] + stair_list[i - 1] + stair_list[i], dp_list[i - 2] + stair_list[i])
    
    print(dp_list[-1])