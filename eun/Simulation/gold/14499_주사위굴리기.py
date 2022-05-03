# 14499 주사위 굴리기
# 220503

n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in move:
    nx = x+dx[i]
    ny = y+dy[i]

    if nx >= 0 and ny >= 0 and nx < n and ny < m:
        x, y = nx, ny
        if i == 1:
            dice = [dice[3]]+[dice[1]]+[dice[0]]+[dice[5]]+[dice[4]]+[dice[2]]
        elif i == 2:
            dice = [dice[2]]+[dice[1]]+[dice[5]]+[dice[0]]+[dice[4]]+[dice[3]]
        elif i == 3:
            dice = [dice[4]]+[dice[0]]+[dice[2]]+[dice[3]]+[dice[5]]+[dice[1]]
        elif i == 4:
            dice = [dice[1]]+[dice[5]]+[dice[2]]+[dice[3]]+[dice[0]]+[dice[4]]

        if grid[x][y] == 0:
            grid[x][y] == dice[-1]
        else:
            dice[-1] = grid[x][y]
            grid[x][y] = 0
        print(dice[0])
