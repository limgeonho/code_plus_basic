# 골드바흐의 추측

# def check(x):
#     if x == 1:
#         return False
#     else:
#         for i in range(2, x):
#             if x % i == 0:
#                 return False
#     return True
r = 1000000

check = [True for _ in range(r)]

for i in range(2, int(r**0.6)):
    if check[i] == True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] = False


while True:
    n = int(input())
    a = 0
    b = 0
    if n == 0:
        break
    else:
        for i in range(3, r):
            if check[i] and check[n-i]:
                a = n-i
                b = i
                break
        else:
            continue
    print(f"{n} = {b} + {a}")
