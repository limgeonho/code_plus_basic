# 연속합

n = int(input())

array = list(map(int, input().split()))


dp = array[:]

for i in range(n):
    if i == 0:
        continue
    if dp[i] < dp[i-1] + array[i]:
        dp[i] = dp[i-1] + array[i]

print(max(dp))