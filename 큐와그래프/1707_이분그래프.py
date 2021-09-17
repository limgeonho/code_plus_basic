# 이분 그래프

k = int(input())


for _ in range(k):
    v, e = map(int, input().split())

    array = [[]*(v+1)for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        array[a].append(b)
        array[b].append(a)

    #########################################