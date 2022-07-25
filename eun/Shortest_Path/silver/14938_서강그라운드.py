import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
table = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    table[a][b] = c
    table[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                table[i][j] = 0
            table[i][j] = min(table[i][j], table[i][k]+table[k][j])
res = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if table[i][j] <= m:
            temp += items[j]
    if temp > res:
        res = temp

print(res)

# 모든 정잠으로부터 모든 정점까지의 거리를 구해야 하므로 플로이드 워셜
# 플로이드 워셜 알고리즘으로 모든 정점까지의 최단 거리를 구한 후
# 각 정점을 돌면서 도달할 수 있는 정점의 item수를 더해 주었다.
# 그리고 최대 item수로 갱신해주었다.
