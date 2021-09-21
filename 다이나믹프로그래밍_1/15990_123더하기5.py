# 1, 2, 3 더하기 5

import heapq

h = []
heapq.heappush(h, (3, 'third'))
heapq.heappush(h, (4, 'fourth'))
heapq.heappush(h, (2, 'second'))
heapq.heappush(h, (5, 'fifth'))
# heapq.heappush(h, (1, 'first'))

print(h)

for _ in range(len(h)):
    print(heapq.heappop(h))