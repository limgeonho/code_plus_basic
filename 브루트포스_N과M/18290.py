# NM과 K

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n, m, l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
max_num = -2147000000


def go(cnt, total):
    if cnt == l:
        global max_num
        if total > max_num:
            max_num = total
        return
    for i in range(n):
        for j in range(m):
            if check[i][j] == True:
                continue
            flag = True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if check[nx][ny] == True:
                        flag = False
            if flag == True:
                check[i][j] = True
                go(cnt+1, total+board[i][j])
                check[i][j] = False


go(0, 0)

print(max_num)
