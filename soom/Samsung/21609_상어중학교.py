# 검은 블록 -1, 무지개 블록 0
# 일반 블록끼리 하나의 그룹을 형성해야 하며, 무지개 블록은 얼마든지 포함가능
# 그룹 >= 2, 모두 연결되어 있어야 한다.(대각선x)
# 기준 블록 = 무지개 블록이 아닌 블록(block != 0) 중 행의 번호가 가장 작은 블록, 그 다음 열의 번호가 가장 작은 블록(정렬?)
# -> 0,0 부터 돌아다니면서 무지개나 검은 블록이 아닌 것을 찾아, 연결된 블록을 구성한다.
# 크기가 가장 큰 블록 그룹을 찾는다. 무지개가 많은 그룹, 기준 블록의 행이 큰 것, 열이 큰 것 순으로 우선순위이다.
# 블록 그룹에 포함된 블록의 수 = B, B**2점을 획득
# 중력 -> -1을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동 (다른 블록이나 격자의 경계를 만나기 전까지 지속)
# 90도 회전
# 중력
# 다시 블록 그룹 찾기

from collections import deque


# 인접 블록 찾기 -> 블록 크기, 무지개크기, 블록좌표 리턴
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0  # 블록개수, 무지개블록 개수
    blocks, rainbows = [[x, y]], []  # 블록좌표 넣을 리스트, 무지개좌표 넣을 리스트

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 안이면서 방문 안한 일반 블록인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and a[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            # 범위 안이면서 방문 안한 무지개 블록인 경우
            elif 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and a[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개블록은 방문 다시 해제
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]


# 블록 제거 함수
def remove(block):
    for x, y in block:
        a[x][y] = -2


# 중력 함수
def gravity(a):
    for i in range(N - 2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if a[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0 <= r + 1 < N and a[r + 1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r + 1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break


# 반시계 회전 함수
def rot90(a):
    new_a = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_a[N - 1 - j][i] = a[i][j]
    return new_a


# 0. 메인코드
N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

score = 0  # 점수

# 1. 오토플레이-> while {2. 크기 가장 큰 블록 찾기 3. 블록제거+점수더하기 4. 중력 5. 90회전 6. 중력}
while True:
    # 2. 크기 가장 큰 블록 찾기
    visited = [[0] * N for _ in range(N)]  # 방문체크
    blocks = []  # 가능한 블록 그룹들 넣을 리스트
    for i in range(N):
        for j in range(N):
            if a[i][j] > 0 and not visited[i][j]:  # 일반블록이면서 방문 안했으면
                visited[i][j] = 1  # 방문
                block_info = bfs(i, j, a[i][j])  # 인접한 블록 찾기
                # block_info = [블록크기, 무지개블록 개수, 블록좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 3. 블록제거+점수더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0] ** 2

    # 4. 중력
    gravity(a)

    # 5. 90회전
    a = rot90(a)

    # 6. 중력
    gravity(a)

print(score)