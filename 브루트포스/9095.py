# 1, 2, 3 더하기

array = [1, 2, 4]
for i in range(3, 12):
    array.append(array[i-1] + array[i-2] + array[i-3])

T = int(input())
for _ in range(T):
    n = int(input())
    print(array[n-1])

