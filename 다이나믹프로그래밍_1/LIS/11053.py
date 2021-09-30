# 가장 긴 증가하는 부분수열

from bisect import bisect_left

# n = int(input())
#
# array = list(map(int, input().split()))
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j]+1)
#
# print(max(dp))

n = int(input())

array = list(map(int, input().split()))

dp = [array[0]]

for i in range(1, n):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        dp[bisect_left(dp, array[i])] = array[i]

print(len(dp))