# 11265 끝나지 않는 파티
# 2022-04-06
import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # N: 파티장의 크기, M: 서비스를 요청한 손님의 수


graph = [list(map(int, input().split())) for _ in range(N)]

# 입력 받을 때 for문을 통해 list.append로 입력을 받는 것 보다
# 리스트 내포(List  Comprehension)를 통해 입력 받는 것이 더 빠름.
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):

            # 최솟값을 갱신할 때 min을 쓰면 작든, 크든 모든 경우에 갱신하므로
            # if 문을 사용했을 때보다 시간이 오래 걸린다.

            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

            # graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")


"""
## 2차시도
정답도 맞게 나오고, 풀이도 맞다고 생각하는데 계속 시간 초과 
-> 중간중간 코드를 다르게 구현해보면서 실험해보기로 함.
"""


# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# N, M = map(int, input().split())  # N: 파티장의 크기, M: 서비스를 요청한 손님의 수

# graph = [[]]
# distance = [[INF]*(N+1) for _ in range(N+1)]
# for _ in range(N):
#     graph.append([0]+list(map(int, input().split())))


# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             distance[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     if distance[a][b] <= c:
#         print("Enjoy other party")
#     else:
#         print("Stay here")


"""
## 1차 시도
다익스트라 알고리즘 방식으로 풀다가 플로이드 워셜 알고리즘으로 풀어야 한다고 깨닫고 주석처리함.
"""
# def dijkstra(start):

#     distance[start] = 0
#     q = []
#     heapq.heappush(q,(0, start))

#     while q:
#         dist, now = heapq.heappop(q)

#         if distance[now]<dist:
#             # 이미 처리 한 노드라면 pass
#             continue

#         for i in range(1,N+1):
#             next_node = i
#             cost = dist+graph[now][i]

#             if i == now:
#                 # 자기 자신이라면 pass
#                 continue


#         if cost<distance[next_node]:
#             distance[next_node] = cost
#             heapq.heappush(q, (cost, next_node))

# dijkstra(1)
