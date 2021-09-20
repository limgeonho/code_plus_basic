# 숨바꼭질4
# 경로추적하는 문제 다시 확인!!

from collections import deque

def path(x):
    arr = []
    tmp = x
    for _ in range(visited[x]+1):
        arr.append(tmp)
        tmp = visited_2[tmp]
    print(visited[k])
    print(' '.join(map(str, arr[::-1])))

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        now = q.popleft()
        if now == k:
            path(now)
            return
        for nxt in (now+1, now-1, 2*now):
            if 0<=nxt<100001 and visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                visited_2[nxt] = now
                q.append(nxt)


n, k = map(int, input().split())
array = [0] * 100001
visited = [-1] * 100001
visited_2 = [-1] * 100001
bfs(n)

