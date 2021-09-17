# ABCDE


def dfs(x, cnt):
    global answer
    if cnt == 5:
        answer = True
        return
    visited[x] = True
    for i in array[x]:
        if not visited[i]:
            dfs(i, cnt+1)
            visited[i] = False


n, m = map(int, input().split())

array = [[] * n for _ in range(n)]

for _ in range(m):
    f1, f2 = map(int, input().split())
    array[f1].append(f2)
    array[f2].append(f1)

visited = [False] * n

answer = False

for i in range(n):
    dfs(i, 1)
    visited[i] = False
    if answer:
        print(1)
        break
else:
    print(0)
