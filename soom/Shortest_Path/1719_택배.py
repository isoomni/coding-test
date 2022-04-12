# a에서 b까지 최적경로(가중치로 구함)의 첫 확정 점을 append
'''
플로이드 워셜 알고리즘
모든 정점 사이의 최단 경로를 찾는 탐색 알고리즘이다.

1. 하나의 정점에서 다른 정점으로 바로 갈 수 있으면 최소 비용을, 갈 수 없다면 INF 배열에 값을 저장한다.
2. 3중 FOR문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값을 바꿔준다.
3. 위의 과정을 반복해 모든 정점 사이의 최단 경로를 탐색한다.
'''

import sys

input = sys.stdin.readline
# 노드의 개수 및 간선의 개수를 입력받기
N, M = map(int, input().split())
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [[0] * (N + 1) for _ in range(N + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# 
for a in range(N + 1):
    for b in range(N + 1):
        if a == b:
            graph[a][b] = 0
            ans[a][b] = INF

for _ in range(M):
    v1, v2, route = map(int, input().split())
    # 양방향 그래프이므로
    graph[v1][v2] = route
    graph[v2][v1] = route
    # v1 출발 -> v2 도착이면 v1 기준으로 v2가 도착지점이 되어야함.
    ans[v1][v2] = v2
    # 위와 반대
    ans[v2][v1] = v1

# 플로이드 워셜 알고리즘 (점화식 이용 --> DP)
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            # 기존의 a -> b로 가는 저장된 비용보다
            # a -> k -> b로 가는 경로가 더 최단 거리이면
            if graph[a][b] > graph[a][k] + graph[k][b]:
                # 비용을 최단 거리로 갱신
                graph[a][b] = graph[a][k] + graph[k][b]
                # 먼저 들러야하는 지점인 (a, k)의 집하장 값으로 갱신
                ans[a][b] = ans[a][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ans[i][j] == INF:
            print('-', end=' ')
        else:
            print(ans[i][j], end=' ')
    print()