n = int(input())

dp = [0] * 36
dp[0] = 1

for i in range(1, n + 1):
    tmp = 0
    for j in range(i // 2):
        tmp += dp[j] * dp[(i - 1 - j)]
    
    if i % 2 == 0:
        tmp = tmp * 2
    else:
        tmp = tmp * 2 + (dp[(i - 1) // 2] ** 2)

    dp[i] = tmp

print(dp[n])