# 그대, 그머가 되어

import heapq

start, end = map(int, input().split())

n, m = map(int, input().split())

distance = [1e9] * (n+1)
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
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


if distance[end] == 1e9:
    print(-1)
else:
    print(distance[end])