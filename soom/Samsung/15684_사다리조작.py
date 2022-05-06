# n, m, h
# 세로, 가로, 가로 가능
# 가로선 정보 (a,b)
# 조작하는 가로선은 얼마든지 더 추가가능
# 결과적으로 +-0이 되어야함.
# 출력: 몇 개의 선을 더 추가해야 하는가?

import sys
sys.stdin = open('soom/Samsung/15684.txt', 'r')

n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    # 모든 열에 대해서 현재 i번째 열이 사다리를 이동해서 i번째에 도착할 수 있는지 확인
    for i in range(1, n+1):

        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:  # 해당 열에 대해서 왼쪽에 만약 사다리가 놓였다면 왼쪽으로 이동하므로 now(이동된 값)을 now-1로 해주고
                now -= 1
            elif visited[j][now]:  # 만약 현재 위치에 사다리가 놓였다면 오른쪽으로 이동해야하므로 now(이동된 값)을 now+1로 해준다
                now += 1
        if now != i:
            return False  # 처음 출발했던 열의 번호와 now(이동된 값)을 비교해서 True, False를 반환
    return True

def dfs(depth, idx):
    global answer
    if depth >= answer:  # 사다리를 3번 이상 놓았을 때도 check()
        return
    if check():    # 모든 열의 값이 사다리를 타고 이동했을 때 자신의 열값과 이동된 값지 않다면 더이상 dfs 를 돌릴 필요 없기 때문에 return
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]: # 사다리를 놓을 수 있는지 확인
            visited[x][y] = True  # 사다리를 놓을 수 있다면 사다리를 놓은 후
            dfs(depth+1, c+1)   # dfs 함수로 재귀를 구현한다.
            visited[x][y] = False


for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)