# 가장 긴 증가하는 부분 수열4

n = int(input())

array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

order = max(dp)

answer = []

for i in range(n-1, -1, -1):
    if dp[i] == order:
        answer.append(array[i])
        order -= 1

print(*answer[::-1])