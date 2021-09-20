# 미로 탐색
import pprint

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = []
    q.append((x, y))
    array[x][y] = '0'
    while q:
        now = q.pop(0)
        if now == (n, m):
            return
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0<=nx<n and 0<=ny<m and array[nx][ny] == '1':
                q.append((nx, ny))
                array[nx][ny] = '0'
                visited[nx][ny] = visited[now[0]][now[1]] + 1

n, m = map(int, input().split())
array = []
visited = [[1]*m for _ in range(n)]
for _ in range(n):
    array.append(list(input()))

bfs(0,0)
# pprint.pprint(visited)
print(visited[n-1][m-1])