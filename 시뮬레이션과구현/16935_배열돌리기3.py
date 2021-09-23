# 배열 돌리기 3


def check(x):
    if x == 1:
        tmp = []
        for i in range(len(array)-1, -1, -1):
            tmp.append(array[i])
        return tmp
    elif x == 2:
        tmp = []
        for i in range(len(array)):
            tmp.append(array[i][::-1])
        return tmp
    elif x == 3:
        tmp = [k[::-1] for k in zip(*array)]
        return tmp
    elif x == 4:
        tmp_2 = []
        tmp_3 = []
        tmp = [k[::-1] for k in zip(*array)]
        for i in range(len(tmp)-1, -1, -1):
            tmp_2.append(tmp[i])
        for i in range(len(tmp_2)):
            tmp_3.append(tmp_2[i][::-1])
        return tmp_3
    elif x == 5:
        row = len(array)
        col = len(array[0])
        tmp = list([0]* col for _ in range(row))
        for i in range(len(array)):
            for j in range(len(array[0])):
                if i < len(array) // 2 and j < len(array[0]) // 2:
                    tmp[i][j + col // 2] = array[i][j]
                elif i < len(array) // 2 and j >= len(array[0]) // 2:
                    tmp[i + row // 2][j] = array[i][j]
                elif i >= len(array) // 2 and j < len(array[0]) // 2:
                    tmp[i - row // 2][j] = array[i][j]
                else:
                    tmp[i][j - col // 2] = array[i][j]
        return tmp
    else:
        row = len(array)
        col = len(array[0])
        tmp = list([0] * col for _ in range(row))
        for i in range(len(array)):
            for j in range(len(array[0])):
                if i < len(array) // 2 and j < len(array[0]) // 2:
                    tmp[i + row // 2][j] = array[i][j]
                elif i < len(array) // 2 and j >= len(array[0]) // 2:
                    tmp[i][j - col // 2] = array[i][j]
                elif i >= len(array) // 2 and j < len(array[0]) // 2:
                    tmp[i][j + col // 2] = array[i][j]
                else:
                    tmp[i - row // 2][j] = array[i][j]
        return tmp

n, m, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

oper = list(map(int, input().split()))

answer = []

for o in oper:
    answer = check(o)
    array = answer[:]

for arr in array:
    print(*arr)

###################################################################
# def operation1(a):
#     n = len(a)
#     m = len(a[0])
#     ans = [[0]*m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             ans[i][j] = a[n-i-1][j]
#     return ans
#
# def operation2(a):
#     n = len(a)
#     m = len(a[0])
#     ans = [[0]*m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             ans[i][j] = a[i][m-j-1]
#     return ans
#
# def operation3(a):
#     n = len(a)
#     m = len(a[0])
#     ans = [[0]*n for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             ans[i][j] = a[n-j-1][i]
#     return ans
#
# def operation4(a):
#     n = len(a)
#     m = len(a[0])
#     ans = [[0]*n for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             ans[i][j] = a[j][m-i-1]
#     return ans
#
# def operation5(a):
#     n = len(a)
#     m = len(a[0])
#     ans = [[0]*m for _ in range(n)]
#     for i in range(n//2):
#         for j in range(m//2):
#             ans[i][j+m//2] = a[i][j]
#             ans[i+n//2][j+m//2] = a[i][j+m//2]
#             ans[i+n//2][j] = a[i+n//2][j+m//2]
#             ans[i][j] = a[i+n//2][j]
#     return ans
#
# def operation6(a):
#     n = len(a)
#     m = len(a[0])
#     ans = [[0]*m for _ in range(n)]
#     for i in range(n//2):
#         for j in range(m//2):
#             ans[i+n//2][j] = a[i][j]
#             ans[i][j] = a[i][j+m//2]
#             ans[i][j+m//2] = a[i+n//2][j+m//2]
#             ans[i+n//2][j+m//2] = a[i+n//2][j]
#     return ans
#
# n,m,r = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# func = [operation1, operation2, operation3, operation4, operation5, operation6]
# for op in map(int, input().split()):
#     a = func[op-1](a)
# for row in a:
#     print(*row, sep=' ')

