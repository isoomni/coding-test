# 20058 마법사 상어와 파이어스톰
# 2022-04-29
import sys
sys.stdin = open('eun/input/20058.txt', 'r')
n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
magic = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(x, y, num):
    turn_list = []
    for i in range(x, x+num):
        turn_list.append(grid[i][y:y+num])
    turn_list = list(map(list, zip(*turn_list[::-1])))
    a = 0
    b = 0
    for i in range(x, x+num):
        for j in range(y, y+num):
            grid[i][j] = turn_list[a][b]
            b += 1
        a += 1
        b = 0


def ice_magic():
    l = []

    for x in range(0, 2**n):
        for y in range(0, 2**n):
            count = 0
            if grid[x][y] > 0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]

                    if nx >= 0 and ny >= 0 and nx < 2**n and ny < 2**n and grid[nx][ny] > 0:
                        count += 1

                if count < 3:
                    l.append((x, y))

    # print(l)
    for i, j in l:
        grid[i][j] -= 1


def solution():
    for L in magic:
        for i in range(0, 2**n, 2**L):
            for j in range(0, 2**n, 2**L):
                turn(i, j, 2**L)

        ice_magic()


def dfs(x, y):
    global max_count
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and ny >= 0 and nx < 2**n and ny < 2**n and grid[nx][ny] > 0 and visited[nx][ny] == False:
            max_count += 1
            dfs(nx, ny)


solution()


ice_sum = 0
for i in range(2**n):
    ice_sum += sum(grid[i])

answer = 0
visited = [[False]*(2**n) for _ in range(2**n)]
for i in range(0, 2**n):
    for j in range(0, 2**n):
        if grid[i][j] > 0 and visited[i][j] == False:
            max_count = 1
            dfs(i, j)
            if answer < max_count:
                answer = max_count

print(ice_sum)
print(answer)
