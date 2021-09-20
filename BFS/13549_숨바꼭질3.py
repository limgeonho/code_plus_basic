# 숨바꼭질3

from collections import deque

def bfs(x):
    q = deque()
    visited[x] = 0
    q.append(x)
    while q:
        now = q.popleft()
        nxt_2 = now * 2
        # if now == k:
        #     return
        if 0<=nxt_2<100001 and visited[nxt_2] == -1:
            visited[nxt_2] = visited[now]
            q.append(nxt_2)
        for nxt in (now+1, now-1):
            if 0<= nxt < 100001 and visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

n, k = map(int, input().split())

array = [-1] * 100001
visited = [-1] * 100001

bfs(n)
print(visited)