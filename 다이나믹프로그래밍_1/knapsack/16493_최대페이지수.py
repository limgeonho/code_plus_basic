# 최대 페이지 수

n, m = map(int, input().split())
dp = [0] * (n+1)

for _ in range(m):
    day, pages = map(int, input().split())
    for i in range(n, day-1, -1):
        dp[i] = max(dp[i], dp[i-day] + pages)

print(dp[n])