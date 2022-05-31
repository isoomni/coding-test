# n, m = map(int, input().split())

# grid = [list(map(int, input().split())) for _ in range(n)]

# move = [[(-1, 0), (0, -1)], [(-1, 0), (0, 1)],
#         [(0, -1), (1, 0)], [(0, 1), (1, 0)]]


# def check(x, y):
#     if x >= 0 and y >= 0 and x < n and y < n:
#         return True
#     return False


# def back(x, y, visited, answer):
#     if x >= n and y >= m:
#         result.append(answer)
#         return

#     if visited[x][y] == False:
#         visited[x][y] = True
#         for i in range(4):
#             nx1 = x+move[i][0][0]
#             ny1 = x+move[i][0][1]
#             nx2 = x+move[i][1][0]
#             ny2 = x+move[i][1][1]

#             if check(nx1, ny1) and visited[nx1][ny1] == False and check(nx2, ny2) and visited[nx2][ny2] == False:
#                 visited[nx1][ny1] = True
#                 visited[nx2][ny2] = True
#                 answer += (grid[x][y]*2)+grid[nx1][ny1]+grid[nx2][ny2]
#                 back(x, y+1, visited, answer)
#                 back(x+1, y, visited, answer)


# result = []
# visited = [[False]*m for _ in range(n)]
# back(0, 0, visited, 0)


# x행 y열을 idx로 변환하기 위한 함수
def calcIdx(x, y):
    return x * M + y


# idx: 현재 (행 ,열) 위치의 인덱스, sum: 지금까지 만든 부메랑들의 강도의 합
def solve(idx, sum):
    if idx == N * M:  # 마지막에 도달했을 때
        global result
        result = max(result, sum)  # 최댓값을 갱신하고 탐색 종료
        return

    if check[idx]:  # 이미 부메랑을 만드는 데 사용된 칸일 경우에는 탐색 종료
        return

    # 현재 idx에 대한 행과 열
    x = idx // M
    y = idx % M

    # 현재 idx를 기준으로 오른쪽(east), 왼쪽(west), 아래쪽(south), 위쪽(north)에 대한 idx
    eastIdx = calcIdx(x, y+1)
    westIdx = calcIdx(x, y-1)
    southIdx = calcIdx(x+1, y)
    northIdx = calcIdx(x-1, y)

    # ㅁㅁ
    # ㅁ   형태의 부메랑을 만들 수 있는지 확인
    if (x+1 < N and not check[southIdx]) and (y+1 < M and not check[eastIdx]):
        # 만들 수 있을 경우 해당 칸들을 사용했음을 체크하고
        # 현재 idx 이후부터 마지막 idx까지 반복적으로 호출
        check[idx] = True
        check[southIdx] = True
        check[eastIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x+1][y] + board[x][y+1]))
        check[southIdx] = False
        check[eastIdx] = False
        check[idx] = False

    # ㅁㅁ
    #  ㅁ  형태의 부메랑을 만들 수 있는지 확인
    if (y-1 >= 0 and not check[westIdx]) and (x+1 < N and not check[southIdx]):
        check[idx] = True
        check[westIdx] = True
        check[southIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x][y-1] + board[x+1][y]))
        check[westIdx] = False
        check[southIdx] = False
        check[idx] = False

    #   ㅁ
    # ㅁㅁ 형태의 부메랑을 만들 수 있는지 확인
    if (y-1 >= 0 and not check[westIdx]) and (x-1 >= 0 and not check[northIdx]):
        check[idx] = True
        check[westIdx] = True
        check[northIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x][y-1] + board[x-1][y]))
        check[westIdx] = False
        check[northIdx] = False
        check[idx] = False

    # ㅁ
    # ㅁㅁ 형태의 부메랑을 만들 수 있는지 확인
    if (x-1 >= 0 and not check[northIdx]) and (y+1 < M and not check[eastIdx]):
        check[idx] = True
        check[northIdx] = True
        check[eastIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x-1][y] + board[x][y+1]))
        check[northIdx] = False
        check[eastIdx] = False
        check[idx] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [False for _ in range(N*M)]
result = 0

for i in range(N*M):
    solve(i, 0)

print(result)
