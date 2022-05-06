# 3, 11, 13, 16, 31번 미통과
def check_range(x, y, n):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def check(place):
    grid = [list(place[i]) for i in range(len(place))]

    dist1_dx = [1, 0]  # 밑, 오른쪽(거리 1)
    dist1_dy = [0, 1]

    dist2_dx = [2, 0]  # 밑, 오른쪽(거리 2)
    dist2_dy = [0, 2]

    dist2_dx2 = [1, 1]  # 오른쪽 아래, 왼쪽 아래
    dist2_dy2 = [1, -1]
    dist2_check = [[0, 1, 1, 0], [1, 0, 0, -1]]  # 격자 확인

    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == "P":
                for i in range(2):
                    nx = x+dist1_dx[i]
                    ny = y+dist1_dy[i]

                    if check_range(nx, ny, len(grid)) and grid[nx][ny] == "P":
                        return 0

                for i in range(2):
                    nx = x+dist2_dx[i]
                    ny = y+dist2_dy[i]

                    if check_range(nx, ny, len(grid)) and grid[nx][ny] == "P":
                        if grid[x+dist1_dx[i]][y+dist1_dy[i]] != "X":  # 사이에 벽이 없으면
                            return 0

                for i in range(2):
                    nx = x+dist2_dx2[i]
                    ny = y+dist2_dy2[i]

                    if check_range(nx, ny, len(grid)) and grid[nx][ny] == "P":
                        if not (grid[x+dist2_check[i][0]][y+dist2_check[i][1]] == "X" and grid[x+dist2_check[i][2]][y+dist2_check[i][3]] == "X"):
                            return 0

    return 1


def solution(places):
    answer = []

    for i in range(len(places)):
        result = check(places[i])
        answer.append(result)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
