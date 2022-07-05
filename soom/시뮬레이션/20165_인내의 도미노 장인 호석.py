from sys import stdin
input = stdin.readline

# (시작 위치, 방향, 길이) 인자로 넘기면 재귀로 도미노 넘기기
def domino(sr, sc, sd, length):
    global temp # 도미노 갯수 temp
    if board[sr][sc]:
        board[sr][sc] = 0 # 값이 있을 때만 0으로 바꿔주면서 매 라운드별로 넘기는 도미노 갯수 temp를 갱신해준다.
        temp += 1
    for dis in range(length-1):
        sr += dirInfo[sd][0]
        sc += dirInfo[sd][1]
        if not (0 <= sr < N and 0 <= sc < M):
            continue
        domino(sr, sc, sd, board[sr][sc])

# main
N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
raw = [row[:] for row in board]  # 수비할 때, 원래 맵에 있는 도미노 정보로 복원해줘야 하기 때문에 raw배열에 board맵을 복사해놓는다.
dirInfo = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)} # 동서남북 E, W, S, N에 대해 이동하는 델타 좌표 dirInfo에 딕셔너리로 미리 저장해둔다.

total = 0	# 넘어뜨린 도미노 갯수 총합
for game in range(R):
    off_r, off_c, off_d = input().split()
    def_r, def_c = map(int, input().split())
    off_r = int(off_r) - 1
    off_c = int(off_c) - 1
    def_r -= 1
    def_c -= 1

    # 공격 : 도미노 넘기기
    temp = 0
    if board[off_r][off_c]:
        domino(off_r, off_c, off_d, board[off_r][off_c])

    # 수비 : 도미노 세우기
    board[def_r][def_c] = raw[def_r][def_c]
    total += temp

# 정답 출력
print(total)
for r in range(N):
    for c in range(M):
        if board[r][c]:
            board[r][c] = "S"
        else:
            board[r][c] = "F"
    print(*board[r])