# 리모컨
# 최소값 찾기(불필요한 값, 중복되는 값들은 철저하게 배제)
# 어느쪽이 최소 경우인지는 알수 없다 -> 다해봐야함(브루트포스)

n = input()
m = int(input())
arr = set(list(map(int, input().split())))

tmp = ''
cnt = 0
can_use = set(list(range(0, 10))) - arr
print(can_use)
can_use_list = list(can_use)

for i in range(len(n)):
    if int(n[i]) in can_use:
        tmp += n[i]

    else:
        if i > 0 and ((can_use_list[i+1] - can_use_list[i]) > (can_use_list[i] - can_use_list[i-1])):
            if can_use_list[i-1] == 0:
                continue
            tmp += str(can_use_list[i-1])
        else:
            tmp += str(can_use_list[i+1])

print(tmp)