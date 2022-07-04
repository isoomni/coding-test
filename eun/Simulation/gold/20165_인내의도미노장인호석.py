import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
action = [list(map(str, input().split())) for _ in range(r*2)]
board = [["S"]*m for _ in range(n)]

direction = {"E": (0, 1), "N": (-1, 0), "W": (0, -1), "S": (1, 0)}


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def offensive(x, y, move):
    res = 1  # 쓰러트린 개수
    cnt = arr[x][y]-1  # 앞으로 넘어질 개수
    board[x][y] = "F"
    while cnt > 0:
        nx = x+direction[move][0]
        ny = y+direction[move][1]
        if check_range(nx, ny):
            if board[nx][ny] == "S":  # 다음 칸이 도미노가 있다면
                board[nx][ny] = "F"  # 쓰러뜨리기
                res += 1  # 횟수 증가
                if arr[nx][ny] > cnt:  # 만약, 방금 쓰러뜨린 도미노가, 앞으로 넘어질 도미노의 개수보다 크다면
                    cnt = arr[nx][ny]  # 넘어질 도미도 개수 갱신
            cnt -= 1  # 쓰러뜨렸거나, F여도 길이 하나 감소
            x, y = nx, ny
        else:
            break  # 범위 벗어나면 break
    return res


answer = 0
for i in range(0, r*2, 2):
    x, y, move = int(action[i][0])-1, int(action[i][1])-1, action[i][2]

    if board[x][y] == "S":
        answer += offensive(x, y, move)

    x2, y2 = int(action[i+1][0])-1, int(action[i+1][1])-1
    if board[x2][y2] == "F":
        board[x2][y2] = "S"

print(answer)
for a in board:
    print(*a)
