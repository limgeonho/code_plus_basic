# N과 M(7)
from itertools import product

n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

for i in product(array, repeat=m):
    print(*i)
