# 소수 찾기


def check(x):
    if x == 1:
        return False
    for a in range(2, int(x**0.5)+1):
        if x % a == 0:
            return False
    return True


n = int(input())
array = list(map(int, input().split()))
cnt = 0
for num in array:
    if check(num):
        cnt += 1
print(cnt)