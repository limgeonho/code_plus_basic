# 숨바꼭질3
# deque의 appendleft()를 기억하기!! => deque의 왼쪽에 넣기 때문에 append()보다 앞으로 들어가고 pop()했을 때 우선적으로 처리 가능하다!

from collections import deque

def bfs(x):
    q = deque()
    array[n] = 0
    visited[n] = True
    q.append(x)

    while q:
        now = q.popleft()

        if now*2 < 200000 and not visited[now*2]:
            visited[now*2] = True
            array[now*2] = array[now]
            q.appendleft(now*2)
        if now-1 >= 0 and not visited[now-1]:
            visited[now-1] = True
            array[now-1] = array[now] + 1
            q.append(now-1)
        if now+1 <200000 and not visited[now+1]:
            visited[now+1] = True
            array[now+1] = array[now] + 1
            q.append(now+1)

n, k = map(int, input().split())

array = [-1] * 200000
visited = [False] * 200000


bfs(n)
print(array[k])