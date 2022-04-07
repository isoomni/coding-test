# 16918 봄버맨
# 2022-04-07
from collections import deque
import heapq
import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())
grid = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < R and y < C:
        return True
    return False


def create_boom(queue):
    # 폭탄 채우기
    for i in range(R):
        for j in range(C):
            if grid[i][j] == ".":
                grid[i][j] = "O"
                # queue.append((i, j, 1))
                heapq.heappush(queue, (1, i, j))


def boom_boom(x, y):
    # 폭탄 터짐
    grid[x][y] = "."
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if check_range(nx, ny) and grid[nx][ny] == "O":
            grid[nx][ny] = "."


def update_grid(queue1, queue2):
    while queue1:
        # x, y, boom = q.popleft()
        boom, x, y = heapq.heappop(queue1)

        if boom == 3:
            boom_boom(x, y)
        else:
            if grid[x][y] == "O":
                heapq.heappush(queue2, (boom+1, x, y))
            # q2.append((x, y, boom+1))


def bfs(q, q2, second):

    while second < N:

        if second % 2 != 0:
            # 폭탄 채우기
            if q:
                update_grid(q, q2)
                create_boom(q2)
            else:
                update_grid(q2, q)
                create_boom(q)

        else:
            if q:
                update_grid(q, q2)
            else:
                update_grid(q2, q)

        # print("\n-------------", second+1)
        # for i in range(R):
        #     print(grid[i])

        second += 1


# q = deque()
# q2 = deque()
q = []
q2 = []
# 초기 세팅
for i in range(R):
    for j in range(C):
        if grid[i][j] == "O":
            heapq.heappush(q, (2, i, j))
            # q.append((i, j, 2))

bfs(q, q2, 1)

for i in range(R):
    print("".join(grid[i]))
