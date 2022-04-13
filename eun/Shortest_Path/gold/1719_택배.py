# 1719 택배
# 2022-04-10

# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# N, M = map(int, input().split())

# result = [[0]*(N+1) for _ in range(N+1)]  # 결과 테이블
# graph = [[] for _ in range(N+1)]


# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))  # 양방향
#     graph[b].append((a, c))


# def dijkstra(start):
#     q = []
#     # 시작 노드 초기화
#     heapq.heappush(q, (0, start))
#     distance = [[INF, 0] for _ in range(N+1)]
#     distance[start] = [0, 0]
#     result[start][start] = "-"

#     for i in graph[start]:
#         # 시작노드에서 처음 도착하는 노드 초기화
#         next_node = i[0]
#         next_node_cost = i[1]

#         distance[next_node] = [next_node_cost, next_node]
#         heapq.heappush(q, (next_node_cost, next_node))
#         result[start][next_node] = next_node

#     while q:
#         dist, now = heapq.heappop(q)

#         for i in graph[now]:
#             next_node = i[0]
#             next_node_cost = i[1]

#             cost = distance[now][0]+next_node_cost

#             if distance[next_node][0] <= dist:  # 이미 방문한 노드는 continue
#                 continue

#             if distance[next_node][0] > cost:
#                 # 최단 거리 갱신
#                 # distance[next_node] 에는 [거리, 이전 노드에 오기까지 가장 먼저 도달한 노드]
#                 distance[next_node] = [cost, distance[now][1]]
#                 heapq.heappush(q, (cost, next_node))
#                 result[start][next_node] = distance[now][1]


# for i in range(1, N+1):
#     dijkstra(i)

# for i in range(1, N+1):
#     print(' '.join(map(str, result[i][1:])))

# 플로이드 워셜
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

distance = [[INF]*(N+1) for _ in range(N+1)]
result = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    distance[b][a] = c
    result[a][b] = b
    result[b][a] = a


for i in range(1, N+1):
    distance[i][i] = 0
    result[i][i] = "-"

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):

            if distance[i][j] > distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k]+distance[k][j]
                result[i][j] = result[i][k]

for i in range(1, N+1):
    print(' '.join(map(str, result[i][1:])))
