# 가장 긴 증가하는 부분 수열5(끝판왕)

from bisect import bisect_left

n = int(input())
array = [0] + list(map(int, input().split()))
tmp = [-1000000001]
dp = [0] * (n+1)
max_val = 0

for i in range(1, n+1):
    if tmp[-1] < array[i]:
        tmp.append(array[i])
        dp[i] = len(tmp) - 1
        max_val = dp[i]
    else:
        # tmp[bisect_left(tmp, array[i])] = array[i]
        dp[i] = bisect_left(tmp, array[i])
        tmp[dp[i]] = array[i]

print(max_val)

answer = []

for i in range(n, 0, -1):
    if dp[i] == max_val:
        answer.append(array[i])
        max_val -= 1

print(*answer[::-1])