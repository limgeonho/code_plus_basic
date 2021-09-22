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

#####################################################

inf = 10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
d = [-1]*(n+1)
for i in range(1, n+1):
    t[i],p[i] = map(int,input().split())
ans = 0
def go(day):
    if day == n+1:
        return 0
    if day > n+1:
        return -inf
    if d[day] != -1:
        return d[day]
    t1 = go(day+1) # x
    t2 = p[day] + go(day+t[day]) # o
    d[day] = max(t1,t2)
    return d[day]

print(go(1))
