# 가장 긴 증가하는 부분 수열3

from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))
dp = [array[0]]

for i in range(1, n):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        dp[bisect_left(dp, array[i])] = array[i]

result = len(dp)
print(result)