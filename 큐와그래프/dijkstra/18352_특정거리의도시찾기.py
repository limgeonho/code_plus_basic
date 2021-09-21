# 특정 거리의 도시 찾기

import heapq

n, m, k, x = map(int, input().split())

distance = [1e9] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra():
    q = []
    distance[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra()

answer = []

for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for num in answer:
        print(num)