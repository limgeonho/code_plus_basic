# 연속합 2

n = int(input())

array = list(map(int, input().split()))

dp_1 = array[:]
dp_2 = array[:]

for i in range(n):
    if i == 0:
        continue
    if dp_1[i] < dp_1[i-1] + array[i]:
        dp_1[i] = dp_1[i-1] + array[i]

for i in range(n-1, -1, -1):
    if i == n-1:
        continue
    if dp_2[i] < dp_2[i+1] + array[i]:
        dp_2[i] = dp_2[i + 1] + array[i]

answer = max(dp_1)

for i in range(1, n):
    if answer < dp_1[i-1] + dp_2[i+1]:
        answer = dp_1[i-1] + dp_2[i+1]
print(answer)