import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]

dx = [1, 0, -1, 1]
dy = [0, 1, 1, 1]


def check_range(x, y):  # 범위 확인
    if x >= 0 and y >= 0 and x < 19 and y < 19:
        return True
    return False


def check(x, y):
    now_x, now_y = x, y
    # 아래, 오른쪽, 우상향, 우하향 순으로 확인 , 좌하향순이나 좌상향 순으로 확인하면 나중에 좌표를 출력할 때 문제가 발생하기 때문에 우상향, 우하향 순으로 확인해야 함.
    for k in range(4):
        x, y = now_x, now_y
        cnt = 0
        while check_range(x, y) and arr[x][y] == arr[now_x][now_y]:
            cnt += 1
            x = x+dx[k]
            y = y+dy[k]

        if cnt == 5 and arr[now_x+(dx[k]*(-1))][now_y+(dy[k]*(-1))] != arr[now_x][now_y]:
            # 만약 6개가 (1,1),(2,1),(3,1),(4,1),(5,1),(6,1) 로 이어져 있을 때,
            # (1,1)에서 검사를 하면 당연히 False가 나오겠지만,
            # (5,1)에서 감사를 하면 True가 나올 수 있음.
            # 따라서 이전의 돌이 연결되어 있는지 확인해야 함.
            # 각 방향의 반대방향은 dx, dy에 -1을 곱해주면 됨.
            return True
    return False


white = False
black = False
res_x, res_y = 0, 0

for i in range(19):
    for j in range(19):
        if not black and arr[i][j] == 1:  # 까만 돌이 아직 승리하지 않았을 때
            black = check(i, j)
            if black:
                res_x, res_y = i, j

        elif not white and arr[i][j] == 2:  # 하얀 돌이 아직 승리하지 않았을 때
            white = check(i, j)
            if white:
                res_x, res_y = i, j

if black and not white:
    print(1)
    print(res_x+1, res_y+1)
elif not black and white:
    print(2)
    print(res_x+1, res_y+1)
else:
    print(0)
