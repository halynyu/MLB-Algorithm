n = int(input())
arr = [float(input()) for _ in range(n)]
    
dp = [0] * n
dp[0] = arr[0]

for i in range(n-1):
    dp[i+1] = max(dp[i] * arr[i+1], arr[i+1])

print(f"{max(dp):.3f}")