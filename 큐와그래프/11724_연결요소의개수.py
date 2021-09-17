# 연결 요소의 개수


def dfs(x):
    visited[x] = True
    for i in array[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


n, m = map(int, input().split())

array = [[]*(n+1)for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)