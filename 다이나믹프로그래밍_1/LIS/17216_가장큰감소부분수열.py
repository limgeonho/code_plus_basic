# 가장 큰 감소 부분 수열

n = int(input())
array = list(map(int, input().split()))

dp = array[:]

for i in range(1, n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))