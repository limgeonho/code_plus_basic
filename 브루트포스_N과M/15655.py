# N과 M(6)
from itertools import combinations

n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

for i in combinations(array, m):
    print(*i)
