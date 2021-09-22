# 포도주 시식
# 2차원 리스트로 관계식세우는 것 연습...

n = int(input())
array = [0]

for _ in range(n):
    array.append(int(input()))

dp = [0] * (n+1)
dp[1] = array[1]

if n >= 2:
    dp[2] = array[1] + array[2]

for i in range(3, n+1):
    dp[i] = dp[i-1]
    dp[i] = max(dp[i], dp[i-2] + array[i])
    dp[i] = max(dp[i], dp[i-3] + array[i] + array[i-1])

print(dp[n])