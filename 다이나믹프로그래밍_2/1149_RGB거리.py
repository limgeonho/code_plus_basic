# RGB거리
# 1, 2, 3 더하기 5와 상당히 유사한 문제... => 2차원 리스트를 이용한 dp

n = int(input())
dp = [[0, 0, 0] for _ in range(n+1)]
houses = [[0, 0, 0]]

for i in range(n):
    houses.append(list(map(int, input().split())))

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))