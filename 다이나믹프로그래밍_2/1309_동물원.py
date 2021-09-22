# 동물원
# dp2의 문제들은 단순하게 규칙을 찾는 것이 아니라 문제를 논리적으로 나누고 이를 리스트에 기준을 정한 뒤에 계산하는 방법


n = int(input())
dp = [[0, 0, 0] for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][0] + dp[i-1][1]
    for j in range(3):
        dp[i][j] %= 9901

print(sum(dp[n]) % 9901)