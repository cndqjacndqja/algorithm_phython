n = int(input())

dp = [0 for _ in range(n+1)]
data = [0]
for _ in range(n):
    data.append(int(input()))

if n >= 1:
    dp[1] = data[1]
if n >= 2:
    dp[2] = data[2]+data[1]
if n >= 3:
    dp[3] = max(data[1]+data[3], max(data[1]+data[2], data[2]+data[3]))
if n >= 4:
    for i in range(4, n+1):
        dp[i] = max(dp[i-4]+data[i-1]+data[i-2] , max(dp[i - 2] + data[i], dp[i - 3] + data[i] + data[i - 1]))

print(dp[n])

