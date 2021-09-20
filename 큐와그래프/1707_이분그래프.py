# 이분 그래프
# 다시 확인
# visited -> color -> 0:아직 방문 전 / 1:A번으로 표시 / 2:B번으로 표시

import sys
sys.setrecursionlimit(1000000)
k = int(sys.stdin.readline())


def dfs(x, c):
    color[x] = c
    for y in array[x]:
        if color[y] == 0:
            if not dfs(y, 3-c):
                return False
        elif color[y] == color[x]:
            return False
    return True


for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    color = [0] * v
    array = [[] for _ in range(v)]

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        array[a-1].append(b-1)
        array[b-1].append(a-1)

    answer = True
    for i in range(v):
        if color[i] == 0:
            if not dfs(i, 1):
                answer = False

    if answer:
        print('YES')
    else:
        print('NO')