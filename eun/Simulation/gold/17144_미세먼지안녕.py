# 17144 미세먼지 안녕!
# 2022-04-21

# import sys
# input = sys.stdin.readline
import copy
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())  # RxC 격자판, T초가 지난 후 미세먼지 양
grid = [list(map(int, input().split())) for _ in range(R)]
visited = [[[0]*(T+1) for _ in range(C)] for _ in range(R)]
robot = []

# 시작 초기화
for i in range(R):
    for j in range(C):
        if grid[i][j] == -1:
            robot.append((i, j))
        elif grid[i][j] != -1 and grid[i][j] != 0:
            visited[i][j][0] = grid[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < R and y < C:
        return True
    return False


def spread_pm25(second):

    for x in range(R):
        for y in range(C):
            if visited[x][y][second-1] > 0 and grid[x][y] != -1:
                count = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]

                    if check_range(nx, ny) and grid[nx][ny] >= 0:
                        # 그리드 범위 안에 있고, 공기 청정기가 아닐 때
                        visited[nx][ny][second] += visited[x][y][second-1]//5
                        count += 1

                visited[x][y][second] += visited[x][y][second-1] - \
                    (visited[x][y][second-1]//5)*count


def spread_robot(second):
    robot1_x, robot1_y = robot[0][0], robot[0][1]

    # move1 = copy.deepcopy(visited[robot1_x][:-1])
    # move2 = copy.deepcopy(visited[0][1:])

    for i in range(robot1_x-2, -1, -1):
        visited[i+1][0] = visited[i][0]

    for i in range(1, C):
        visited[0][i-1] = visited[0][i]

    for i in range(1, robot1_x+1):
        visited[i-1][-1] = visited[i][-1]

    for i in range(C-2, -1, -1):
        visited[robot1_x][i+1] = visited[robot1_x][i]

    # visited[robot1_x][1:] = move1
    # visited[0][:-1] = move2

    robot2_x, robot2_y = robot[1][0], robot[1][1]

    # move1 = copy.deepcopy(visited[robot2_x][:-1])
    # move2 = copy.deepcopy(visited[-1][1:])

    for i in range(robot2_x+2, R):  # 4, 5, 6
        visited[i-1][0] = visited[i][0]

    for i in range(1, C):
        visited[-1][i-1] = visited[-1][i]

    for i in range(R-2, robot2_x-1, -1):
        visited[i+1][-1] = visited[i][-1]

    for i in range(C-2, -1, -1):
        visited[robot2_x][i+1] = visited[robot2_x][i]
    # visited[robot2_x][1:] = move1
    # visited[-1][:-1] = move2


for i in range(1, T+1):
    spread_pm25(i)
    spread_robot(i)
    # for i in visited:
    #     print(i)

result = 0
for i in range(R):
    for j in range(C):
        result += visited[i][j][T]

print(result)
