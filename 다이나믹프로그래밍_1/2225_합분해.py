# 합분해
# ...?

mod = 1000000000
n,k = map(int,input().split())
d = [[0]*(n+1) for _ in range(k+1)]
d[0][0] = 1
for i in range(1, k+1):
    for j in range(0, n+1):
        for l in range(0, j+1):
            d[i][j] += d[i-1][j-l]
        d[i][j] %= mod
print(d[k][n])


###############################################
n,k = map(int,input().split())
dp = [[0] * 201 for _ in range(201)]

for i in range(201):
    dp[1][i] = i
    dp[2][i] = i+1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[k][n])
