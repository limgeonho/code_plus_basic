# 퇴사

def DFS(day, result):
    global max_pay
    if day > n:
        return
    if day == n:
        if result > max_pay:
            max_pay = result
        return
    DFS(day+T[day], result+P[day])
    DFS(day+1, result)


n = int(input())
T = []
P = []
result = 0
max_pay = 0
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

DFS(0, 0)

print(max_pay)
