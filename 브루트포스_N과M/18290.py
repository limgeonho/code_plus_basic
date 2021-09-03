# NM과 K

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

min_num = -2147000000

for i in range(n):
    for j in range(m):
