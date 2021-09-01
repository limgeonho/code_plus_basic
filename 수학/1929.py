# 소수 구하기


def check(x):
    if x == 1:
        return False
    for a in range(2, int(x**0.5)+1):
        if x % a == 0:
            return False
    return True


n, m = map(int, input().split())

for num in range(n, m+1):
    if check(num):
        print(num)