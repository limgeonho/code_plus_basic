# 가장 긴 증가하는 부분 수열5(끝판왕)

from bisect import bisect_left

n = int(input())
array = [0] + list(map(int, input().split()))
# bisect_left를 이용해서 LIS길이만 사용하기 위해 이용
tmp = [-1000000001]
# i번째가 가장 마지막 수 일때 LIS길이를 저장
dp = [0] * (n + 1)
max_val = 0

for i in range(1, n + 1):
    if tmp[-1] < array[i]:
        tmp.append(array[i])
        dp[i] = len(tmp) - 1

    else:
        # tmp[bisect_left(tmp, array[i])] = array[i]
        dp[i] = bisect_left(tmp, array[i])
        tmp[dp[i]] = array[i]

# LIS의 길이 == max_val
max_val = max(dp)
print(max_val)
print(dp)
print(tmp)
answer = []

for i in range(n, 0, -1):
    # max_val == order의 시작점 거꾸로 돌것임
    if dp[i] == max_val:
        answer.append(array[i])
        max_val -= 1

print(*answer[::-1])