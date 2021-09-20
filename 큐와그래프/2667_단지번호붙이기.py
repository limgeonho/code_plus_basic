# 단지번호붙이기

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    global tmp
    q = []
    q.append((x, y))
    array[x][y] = '0'
    while q:
        now = q.pop(0)
        tmp += 1
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == '1':
                q.append((nx, ny))
                array[nx][ny] = '0'
n = int(input())

array = []
for _ in range(n):
    array.append(list(input()))
answer = []
cnt = 0
for i in range(n):
    for j in range(n):
        if array[i][j] == '1':
            tmp = 0
            bfs(i, j)
            answer.append(tmp)
            cnt += 1

answer.sort()
print(cnt)
for num in answer:
    print(num)
