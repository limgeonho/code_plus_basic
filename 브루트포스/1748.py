# 수 이어쓰기1
# 자리수 대로 나눠서 적용
n = int(input())
answer = ''
for i in range(1, n+1):
    answer += str(i)
print(len(answer))