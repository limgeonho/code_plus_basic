# 정수삼각형

n = int(input())

array = [[0 for _ in range(n+1)] for _ in range(n+1)]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# tmp에 한 줄 씩 입력받으면서 배열 형성 n*n(삼각형이지만 n*n형태로)
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        array[i][j] = tmp[j-1]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

print(max(dp[-1]))


##############################################################
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for i in range(n)]
d[0][0] = a[0][0]
for i in range(1, n):
    for j in range(0, i+1):
        d[i][j] = d[i-1][j] + a[i][j]
        if j-1 >= 0 and d[i][j] < d[i-1][j-1] + a[i][j]:
            d[i][j] = d[i-1][j-1] + a[i][j]
print(max(d[n-1]))