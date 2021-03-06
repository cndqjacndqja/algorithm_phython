n = int(input())

dp = [(n+1) for _ in range(n+1)]
dp[n] = 0
for i in range(n, 0, -1):
    if i % 5 == 0:
        dp[i//5] = min(dp[i//5], dp[i]+1)
    elif i % 3 ==0:
        dp[i // 3] = min(dp[i // 3], dp[i] + 1)
    elif i % 2 == 0:
        dp[i//2] = min(dp[i//2], dp[i]+1)
    dp[i-1] = min(dp[i-1], dp[i] + 1)

print(dp[1])