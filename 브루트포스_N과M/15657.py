# N과 M(8)
from itertools import combinations_with_replacement

n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

for i in combinations_with_replacement(array, m):
    print(*i)
