# 1719 택배
# 2022-04-10

# 벨만 포드
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# N, M = map(int, input().split())

# distance = [[INF]*(N+1) for _ in range(N+1)]
# result = [[0]*(N+1) for _ in range(N+1)]

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     distance[a][b] = c
#     distance[b][a] = c
#     result[a][b] = b
#     result[b][a] = a


# for i in range(1, N+1):
#     distance[i][i] = 0
#     result[i][i] = "-"

# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if i == j:
#                 continue
#             if distance[i][j] > distance[i][k]+distance[k][j]:
#                 distance[i][j] = distance[i][k]+distance[k][j]
#                 result[i][j] = k
#             elif distance[i][j] == distance[i][k]+distance[k][j]:
#                 if result[i][j] > k:
#                     result[i][j] = k
# for i in range(1, N+1):
#     print(distance[i])
# print("------")
# for i in range(1, N+1):
#     print(result[i])


import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

# distance = [[INF]*(N+1) for _ in range(N+1)]
result = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# for i in range(1, N+1):
#     distance[i][i] = 0
#     result[i][i] = "-"

print(graph)


def dijkstra(start):
    q = []
    distance = [INF] * (N+1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print(graph[1])
        for i in graph[now]:
            if distance[i[0]] <= dist:
                continue
            if distance[i[0]] > distance[now]+i[1]:
                distance[i[0]] = distance[now]+i[1]
                heapq.heappush(q, (distance[now]+i[0], i[1]))
    print(distance)


dijkstra(1)

for i in range(1, N+1):
    for j in range(1, N+1):
        d
        if i == j:
            continue
        if distance[i][j] > distance[i][k]+distance[k][j]:
            distance[i][j] = distance[i][k]+distance[k][j]
            result[i][j] = k
        elif distance[i][j] == distance[i][k]+distance[k][j]:
            if result[i][j] > k:
                result[i][j] = k
for i in range(1, N+1):
    print(distance[i])
print("------")
for i in range(1, N+1):
    print(result[i])
