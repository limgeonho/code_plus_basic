# DFS와 BFS


def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in array[x]:
        if not visited[i]:
            dfs(i)


def bfs(x):
    q = []
    q.append(x)
    visited[x] = True
    while q:
        now = q.pop(0)
        print(now, end=' ')
        for i in array[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n, m, v = map(int, input().split())

array = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

for arr in array:
    arr.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

