# 1600 말이 되고픈 원숭이
# 2022-04-07

from collections import deque
K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
INF = int(1e9)

q_dx = [-2, -1, -2, -1, 1, 2, 2, 1]
q_dy = [-1, -2, 1, 2, -2, -1, 1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < H and y < W:
        return True
    return False


def calculate_shortest():

    q = deque()
    graph = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    q.append((0, 0, K))
    while q:
        x, y, k = q.popleft()
        if x == H-1 and y == W-1:  # 도착 칸에 도달하면 break
            return graph[x][y][k]

        if k > 0:
            # 퀸의 움직임을 사용할 수 있을 때

            for i in range(8):
                nx = x+q_dx[i]
                ny = y+q_dy[i]
                print(nx, ny)
                if check_range(nx, ny) and grid[nx][ny] == 0 and graph[nx][ny][k-1] == 0:
                    # 범위를 벗어나지 않고, 장애물이 아니며, 퀸의 움직임을 아직 쓸 수 있을 때
                    graph[nx][ny][k-1] = graph[x][y][k]+1
                    q.append((nx, ny, k-1))  # k 하나 씀

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if check_range(nx, ny) and grid[nx][ny] == 0 and graph[nx][ny][k] == 0:
                # 범위를 벗어나지 않고, 장애물이 아닐 때
                graph[nx][ny][k] = graph[x][y][k]+1
                q.append((nx, ny, k))  # k 그대로
    return -1


print(calculate_shortest())
