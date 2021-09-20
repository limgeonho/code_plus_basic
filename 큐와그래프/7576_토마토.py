# 토마토
# 그냥 돌리면 시간초과...? -> deque쓰니까 통과...=> queue를 사용할 때는 무조건 deque쓰자!!

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(visited):
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:
                return -1
    else:
        tmp = []
        for v in visited:
            tmp.append(max(v))
        return max(tmp)-1
def dfs():
    q = deque()
    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and array[nx][ny] == 0:
                q.append((nx, ny))
                array[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1

n, m = map(int,input().split())
array = []
for _ in range(m):
    array.append(list(map(int, input().split())))

visited = array[:]
dfs()
print(check(visited))