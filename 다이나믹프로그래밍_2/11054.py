# 가장 긴 바이토닉 부분 수열

n = int(input())

array = list(map(int, input().split()))

dp_1 = [1] * n
dp_2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)


for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if array[i] > array[j]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)


answer = []

for k in range(n):
    answer.append(dp_1[k] + dp_2[k] - 1)

print(max(answer))
