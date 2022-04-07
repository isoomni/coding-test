# 1600 말이 되고픈 원숭이
# 2022-04-07

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
graph = [[[0, 0]]*W for _ in range(H)]

q_dx = [-2, -1, -2, -1, 1, 2, 2, 1]
q_dy = [-1, -2, 1, 2, -2, -1, 1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < H and y < W:
        return True
    return False


def calculate_shortest(x, y):
    move_four = [H*W, K]
    move_chess = [H*W, K]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if check_range(nx, ny) and grid[nx][ny] == 0 and graph[nx][ny][0] != 0:
            # 범위를 벗어나지 않고, 장애물이 아니며, 방문한 기록이 있을 때
            new_move = [graph[nx][ny][0]+1, graph[nx][ny][1]]
            print(new_move)
            if move_four[0] > new_move[0]:
                move_four = new_move
            elif move_four[0] == new_move[0]:
                if move_four[1] > new_move[1]:
                    move_four = new_move
            print(new_move)

    for i in range(8):
        nx = x+q_dx[i]
        ny = y+q_dy[i]

        if check_range(nx, ny) and grid[nx][ny] == 0 and graph[nx][ny][0] != 0 and graph[nx][ny][1] < K:
            new_move = [graph[nx][ny][0]+1, graph[nx][ny][1]+1]
            print(new_move)
            if move_chess[0] > new_move[0]:
                move_chess = new_move

            elif move_chess[0] == new_move[0]:
                if move_chess[1] > new_move[1]:
                    move_chess = new_move
            print(new_move)

    print(move_four)
    print(move_chess)

    graph[x][y] = min(move_four, move_chess)


for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            for z in range(4):
                nx = i+dx[z]
                ny = j+dy[z]
                if check_range(nx, ny) and grid[nx][ny] == 0:
                    graph[nx][ny] = [1, 0]

        else:
            if grid[i][j] == 0:
                calculate_shortest(i, j)
