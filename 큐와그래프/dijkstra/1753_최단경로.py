# 최단경로
# 다익스트라 알고리즘의 매우 기본적인 형태의 문제

import heapq

v, e = map(int, input().split())
start = int(input())

distance = [1e9] * (v+1)

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra():
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
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

for i in range(1, v+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])