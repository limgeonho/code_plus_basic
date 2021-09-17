# 큐
# 다른거는 알겠는데 이 문제 변수 입력 받는게 특이함...
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        queue.append(num)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)