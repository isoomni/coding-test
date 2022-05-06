import sys
from collections import deque
sys.stdin = open('21610.txt', 'r')
input = sys.stdin.readline

# (r, c)는 r행 c열에 있는 바구니, A[r][c]는 r행 c열에 있는 바구니에 저장된 물의 양
# 1번 열과 n번 열이 이어져있다는 것은 board 제한이 없다는 것
# 5x5 격자에서 비바라기를 시전하면 (5,1)(5,2)(4,1)(4,2)에 비구름이 생긴다.
# 구름에 m번 이동을 명령한다.
# d방향으로 s칸 이동
# 기본 방향 8개 상하좌우 대각선
# 해당 칸의 바구니에 물이 1 증가
# 구름이 사라진다.

# 물이 증가한 (r,c)에서 물복사 버그 마법 -> 대각선으로 1만큼 떨어진 칸에 물이 있는 바구니 수만큼 물의 양이 증가
# 이때 board를 넘어가는 애들은 인접한 대각선이 아니다.
# 물 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
# 다시 구름이 생기는 칸은, 물의 양이 2 이상이면서 구름이 사라진 칸이 아닌 칸이다. 이곳에 물의 양이 2 줄어든다.

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir_move = [list(map(int, input().split())) for _ in range(m)]
dx = 0, -1, -1, -1, 0, 1, 1, 1
dy = -1, -1, 0, 1, 1, 1, 0, -1
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
cloud = deque(cloud)

# 1. 구름 이동 + 물 1 증가
def move_rain(dir, dist):
    global n
    size = len(cloud)
    for _ in range(size):
        x, y = cloud.popleft()
        nx = (x + dx[dir] * dist) % n
        ny = (y + dy[dir] * dist) % n
        if 0 > nx:
            nx += n
        if 0 > ny:
            ny += n
        cloud.append((nx, ny))
        # 구름이 사라진 자리를 표시
        visited[nx][ny] = True
        graph[nx][ny] += 1

# 2. 물복사 버그 -> 대각선 조사, 물 있는 바구니 수만큼 물양 증가 + 구름 제거
def dup():
    while cloud:
        # 대각선 검사
        x, y = cloud.popleft()
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                graph[x][y] += 1


for dir, dist in dir_move:
    visited = [[False] * n for _ in range(n)]

    # 1. 구름 이동 후 비 내리기
    move_rain(dir - 1, dist)

    # 2. 물 복사
    dup()

    # 3. 구름 생성 + 물양 2 감소
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and not visited[i][j]:
                cloud.append((i, j))
                graph[i][j] -= 2

# 4. 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 출력
answer = 0
for i in range(n):
    for j in range(n):
        answer += graph[i][j]
print(answer)
