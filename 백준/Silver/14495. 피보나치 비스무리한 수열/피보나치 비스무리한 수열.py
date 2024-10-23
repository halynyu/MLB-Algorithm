n = int(input())

dp = [1] * 118

if n < 4:
    print(dp[n])
else:
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    print(dp[n - 1])