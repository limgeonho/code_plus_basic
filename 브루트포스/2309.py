# 일곱 난쟁이
# 처음에 전체의 합을 구하고 나머지2명을 빼줘가면서 뺀값이 100인지 확인(반대로 생각)
from itertools import combinations
array = []
for _ in range(9):
    array.append(int(input()))

array.sort()
man = list(combinations(array, 7))
real_answer = []

for answer in man:
    if sum(answer) == 100:
        real_answer = answer
        break

for real in real_answer:
    print(real)