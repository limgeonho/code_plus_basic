# ABCDE

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * n

for i in range(n):
    parent[i] = i

for _ in range(m):
    f1, f2 = map(int, input().split())
    union_parent(parent, f1, f2)

print(parent)