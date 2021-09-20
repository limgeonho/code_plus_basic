# 알고스팟
# BFS탐색을 하는데 우선순위가 있어야하는 경우(먼저, 다음: 2가지) => deque의 appendleft()활용!!!

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())

array = [list(map(int, list(input()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            # 기본적인 미로탐색같지만 0으로 표시되어 있는 구간은 전부 거리가 같음
            # => 1이 아닌 0을 만났을 경우를 전부 먼저 q에 넣음 => appendleft()!!!!!!!
            # => 무조건 appendleft()한 array[][] == 0 먼저 순회
            if array[nx][ny] == 0:
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx, ny))
            else:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

print(dist[n-1][m-1])