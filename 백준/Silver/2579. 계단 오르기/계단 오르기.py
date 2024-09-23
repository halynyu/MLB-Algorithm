import sys
input = sys.stdin.readline
n = int(input())

dp = [[0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    a = int(input())
    if i == 1:
        dp[i] = [a, 0]
    else:
        dp[i] = [max(dp[i-2][1]+a, dp[i-2][0]+a), dp[i-1][0]+a]

        
print(max(dp[-1]))