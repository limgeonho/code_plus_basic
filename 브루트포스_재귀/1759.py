# 암호만들기

from itertools import combinations

L, C = map(int, input().split())
password = list(map(str, input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']
answer = []
password.sort()
answer = list(combinations(password, L))
answer.sort()

final_ans = []

for possible in answer:
    cnt = 0
    for s in vowels:
        if s in possible:
            cnt += 1
    if 0 < cnt < L-1:
        final_ans.append(''.join(possible))

for s in final_ans:
    print(s)
