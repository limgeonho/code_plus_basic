# 타일 채우기
# 1*2 타일 채우기와 비슷한 문제이지만 다른 조건이 더 있음.. => dp는 확실하게 모든 조건을 충족시키는 점화식을 만들어야 한다.

n = int(input())

dp = [0] * (n+1)

dp[0] = 1

for i in range(2, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -1, -2):
        dp[i] += dp[j] * 2
print(dp[n])