# 1, 2, 3 더하기

t = int(input())

dp = [0] * 13

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])