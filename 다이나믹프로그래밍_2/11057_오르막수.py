# 오르막 수
# 쉬운 계단 수와 비슷한 문제 => 계단수 복습!!

dp = [[0] * 10 for _ in range(1001)]
mod = 10007
n = int(input())

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= mod

answer = sum(dp[n])
print(answer%mod)