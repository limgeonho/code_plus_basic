# 외판원 순회2

from itertools import permutations


def check(order):
    tmp = 0
    for i in range(n - 1):
        if array[order[i]][order[i + 1]] != 0:
            tmp += array[order[i]][order[i + 1]]
        else:
            return False
    if array[order[-1]][order[0]] == 0:
        return False
    else:
        tmp += array[order[-1]][order[0]]
    return tmp


n = int(input())

min_cost = 2147000000

array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

orders = [i for i in range(n)]
for order in permutations(orders):
    answer = check(order)
    if answer != False:
        if min_cost > answer:
            min_cost = answer

print(min_cost)