# 카잉 달력
# 앞에 날짜 계산과 비슷하지만 같은 방법으로 풀면 시간이 오래 걸림 -> -1 씩 해줘서  %연산을 통한 규칙발견!
n = int(input())
for _ in range(n):
    M, N, x, y = map(int, input().split())
    a = b = 1
    year = 1
    while a != x or b != y:
        if a == M and b == N:
            if x != M and y != N:
                year = -1
            break
        else:
            a += 1
            b += 1
            year += 1
            if a == M+1:
                a = 1
            if b == N+1:
                b = 1
    print(year)