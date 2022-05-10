from collections import deque
# 시작점이 되는 P의 좌표 인덱스를 모두 구해서 start 리스트에 저장
# P의 다음 진행할 위치가 'O'이고 그 지점이 이미 방문하지 않은 곳일 때만 BFS를 진행하면 된다.


def bfs(p):
    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1 # 시작위치 방문 처리

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':  # P의 다음 진행할 위치가 'O'이고 그 지점이 이미 방문하지 않은 곳일 때, 계속 탐색한다.
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:  # 거리가 많이 가깝게 사람이 있으면 0을 return하고 끝낸다.
                       return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))