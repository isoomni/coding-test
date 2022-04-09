# 16236 아기 상어
# 2022-04-09

from collections import deque
import heapq

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
one = []
two = []
three = []
four = []
five = []
six = []
INF = int(1e9)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def check_range(x, y):

    if x >= 0 and y >= 0 and x < N and y < N:
        return True
    return False


def calculate_dist(shark_x, shark_y, shark_size, fish_list):

    distance = [[INF for _ in range(N)] for _ in range(N)]  # 거리 테이블 무한으로 초기화

    distance[shark_x][shark_y] = 0  # 상어 위치 초기화

    q = deque()
    q.append((shark_x, shark_y))  # 상어의 현재 위치

    shortest_x = -1
    shortest_y = -1

    shortest_distance = INF  # 최소 거리 무한으로 초기화

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(nx, ny) and grid[nx][ny] <= shark_size:
                # 범위를 벗어나지 않고, 상어의 크기보다 작거나 같을 경우
                if distance[nx][ny] > distance[x][y]+1:
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx, ny))

    for i in range(len(fish_list)):
        # 먹을 수 있는 물고기의 리스트를 돌면서 가장 가까운 물고기를 찾아냄
        x, y = fish_list[i]
        if distance[x][y] < shortest_distance:  # 거리가 더 가까울 경우
            shortest_distance = distance[x][y]
            shortest_x = x
            shortest_y = y
        elif distance[x][y] == shortest_distance:  # 거리가 같을 때
            if x < shortest_x:  # 더 위에 있을 경우
                shortest_distance = distance[x][y]
                shortest_x = x
                shortest_y = y
            elif x == shortest_x:  # 높이가 같을 경우
                if y < shortest_y:  # 더 왼쪽에 있을 경우
                    shortest_distance = distance[x][y]
                    shortest_x = x
                    shortest_y = y

    return shortest_x, shortest_y, distance


def solution(x, y):
    shark_size = 2  # 상어 크기
    ate_count = 0  # 상어가 먹은 물고기의 개수
    time = 0  # 시간
    grid[x][y] = 0  # 상어의 위치 9 -> 0

    while True:

        if shark_size == 2:  # 상어의 크기가 2일 때
            if not one:  # 먹을 수 있는 물고기가 없다면
                return time  # 종료

        # 먹을 수 있는 물고기의 리스트를 fish_list로 만듦
        if shark_size == 2:
            fish_list = one
        elif shark_size == 3:
            fish_list = one+two
        elif shark_size == 4:
            fish_list = one+two+three
        elif shark_size == 5:
            fish_list = one+two+three+four
        elif shark_size == 6:
            fish_list = one+two+three+four+five
        else:
            fish_list = one+two+three+four+five+six

        if len(fish_list) == 0:  # 먹을 수 있는 물고기의 개수가 없을 때 time 리턴
            return time

        shortest_x, shortest_y, distance = calculate_dist(
            x, y, shark_size, fish_list)  # 먹을 수 있는 물고기 계산

        if shortest_x == -1 or shortest_y == -1:  # 먹을 수 있는 물고기가 없을 때
            return time
        else:
            grid[shortest_x][shortest_y] = 0  # 물고기를 먹음
            # 각각의 리스에 있으면 삭제
            if (shortest_x, shortest_y) in one:
                one.remove((shortest_x, shortest_y))
            elif (shortest_x, shortest_y) in two:
                two.remove((shortest_x, shortest_y))
            elif (shortest_x, shortest_y) in three:
                three.remove((shortest_x, shortest_y))
            elif (shortest_x, shortest_y) in four:
                four.remove((shortest_x, shortest_y))
            elif (shortest_x, shortest_y) in five:
                five.remove((shortest_x, shortest_y))
            elif (shortest_x, shortest_y) in six:
                six.remove((shortest_x, shortest_y))

            x = shortest_x  # 현재 상어의 위치를 바꿈
            y = shortest_y
            ate_count += 1  # 물고기 하나 먹음
            time += distance[shortest_x][shortest_y]  # 시간 추가

        if shark_size == ate_count:  # 만약에 상어의 크기와 먹은 물고기 개수가 같다면
            shark_size += 1  # 상어의 크기 +1
            ate_count = 0  # 먹은 개수 초기화

    return time


for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            x, y = i, j
        elif grid[i][j] == 1:
            one.append((i, j))
        elif grid[i][j] == 2:
            two.append((i, j))
        elif grid[i][j] == 3:
            three.append((i, j))
        elif grid[i][j] == 4:
            four.append((i, j))
        elif grid[i][j] == 5:
            five.append((i, j))
        elif grid[i][j] == 6:
            six.append((i, j))

print(solution(x, y))
