n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
count = 0
def dfs(x, y):
    global count
    # 종료 조건
    if (x, y) == (1, n + 1): # (x , y) = (1, n + 1)이 될 때, 즉 2X2 넴모 사각형 없이 격자판을 전부 채운 상황에 도달한 경우 count에 1을 더해줍니다.
        count += 1
        return

        if x == m:
            nx, ny = 1, y + 1
        else:
            nx, ny = x + 1, y

        # x, y에 네모를 놓지 않은 경우
        dfs(nx, ny)

        # x, y에 네모를 놓을 수 있고 놓는 경우
        if graph[y - 1][x] == 0 or graph[y - 1][x - 1] == 0 or graph[y][x - 1] == 0: # 좌측, 상단, 좌상단 중 하나라도 넴모가 없어야 2X2 넴모 사각형이 생기지 않는다.
            graph[y][x] = 1
            dfs(nx, ny)
            graph[y][x] = 0

dfs(1, 1)
print(count)
