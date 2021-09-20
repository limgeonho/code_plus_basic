# 숨바꼭질

from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        now = q.popleft()
        if now == k:
            return
        for nxt in (now+1, now-1, 2*now):
            if 0<=nxt<100001 and visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)


n, k = map(int, input().split())
array = [0] * 100001
visited = [-1] * 100001
bfs(n)
print(visited[k])