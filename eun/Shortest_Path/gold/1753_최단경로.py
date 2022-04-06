# 1753 최단경로
# 2022-04-06
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())  # N: 노드의 개수, E: 간선의 개수
start = int(input())  # 시작노드

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)  # 최단 거리가 담길 리스트

for _ in range(E):
    a, b, c = map(int, input().split())  # a->b // cost : c
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0  # 시작노드 거리 0으로 초기화
    heapq.heappush(q, (0, start))  # 시작노드 heapq에 삽입 , heapq에는 (거리, 노드)

    while q:  # q가 앖을 때 까지
        dist, now = heapq.heappop(q)  # 가장 최단거리가 짧은 노드 꺼냄

        if distance[now] < dist:  # 현재 노드의 거리가 dist보다 작다면 이미 처리 된 적이 있는 노드
            continue

        for i in graph[now]:
            cost = i[1]+dist  # 다음 노드까지 가는 비용 + 현재노드의 최단거리

            if cost < distance[i[0]]:  # 다음 노드의 최단거리보다 다음 노드까지 가는 비용 + 현재노드의 최단거리가 더 짧다면
                distance[i[0]] = cost  # 갱신
                heapq.heappush(q, (cost, i[0]))  # heapq에 삽입


dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
