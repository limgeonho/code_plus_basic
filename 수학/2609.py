# 최대공약수와 최소공배수
from math import gcd

n, m = map(int, input().split())
print(gcd(n, m))
print(int(n * m / gcd(n, m)))
