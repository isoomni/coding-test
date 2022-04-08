# 1600 말이 되고픈 원숭이
# 2022-04-07
from collections import deque
K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
INF = int(1e9)
graph = [[[INF, 0] for _ in range(W)] for _ in range(H)]

q_dx = [-2, -1, -2, -1, 1, 2, 2, 1]
q_dy = [-1, -2, 1, 2, -2, -1, 1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < H and y < W:
        return True
    return False


def calculate_shortest(x, y, q):
    while q:
        x, y = q.popleft()
        if x == H-1 and y == W-1:
            break

        for i in range(8):
            nx = x+q_dx[i]
            ny = y+q_dy[i]

            if check_range(nx, ny) and grid[nx][ny] == 0 and graph[x][y][1] < K:
                # 범위를 벗어나지 않고, 장애물이 아니며, 퀸의 움직임을 아직 쓸 수 있을 때
                if graph[nx][ny][0] > graph[x][y][0]+1:
                    graph[nx][ny] = [graph[x][y][0]+1, graph[x][y][1]+1]
                    q.appendleft((nx, ny))
                elif graph[nx][ny][0] == graph[x][y][0]+1:
                    if graph[nx][ny][1] > graph[x][y][1]:
                        graph[nx][ny][1] = graph[x][y][1]
                        q.appendleft((nx, ny))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(nx, ny) and grid[nx][ny] == 0:
                # 범위를 벗어나지 않고, 장애물이 아닐 때
                if graph[nx][ny][0] > graph[x][y][0]+1:
                    graph[nx][ny][0] = graph[x][y][0]+1
                    q.append((nx, ny))
                elif graph[nx][ny][0] == graph[x][y][0]+1:
                    if graph[nx][ny][1] > graph[x][y][1]:
                        graph[nx][ny][1] = graph[x][y][1]
                        q.append((nx, ny))


q = deque()
graph[0][0] = [0, 0]
q.append((0, 0))
calculate_shortest(0, 0, q)

if graph[H-1][W-1][0] == INF:
    print(-1)
else:
    print(graph[H-1][W-1][0])
