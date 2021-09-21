# 카드 구매하기2

n = int(input())

array = [0] + list(map(int, input().split()))

dp = [-1] * (n+1)

dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        if dp[i] == -1 or dp[i] > dp[i-j] + array[j]:
            dp[i] = dp[i-j] + array[j]

print(dp[n])