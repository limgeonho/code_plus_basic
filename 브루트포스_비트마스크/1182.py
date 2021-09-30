# 부분수열의 합

# n, s = map(int, input().split())
# array = list(map(int, input().split()))
# cnt = 0
# for i in range(1, 1<<n):
#     total = 0
#     for j in range(n):
#         if i&(1<<j):
#             total += array[j]
#     if total == s:
#         cnt += 1
# print(cnt)

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))
house.sort()
# house = [1 2 4 8 9]

min_gap = 1
max_gap = house[-1] - house[0]
result = 0

while (min_gap <= max_gap):
    mid = (max_gap + min_gap) // 2
    value = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= value + mid:
            value = house[i]
            count += 1
    if count >= c:
        min_gap = mid + 1
        result = mid
    else:
        max_gap = mid -1

print(result)