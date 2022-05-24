# n, m = map(int, input().split())

# dx = [(0, -1, -1), (-1, -1, 0), (0, 1, 1), (1, 1, 0)]
# dy = [(-1, -1, 0), (0, 1, 1), (1, 1, 0), (0, -1, -1)]


# def check_range(x, y):
#     if x >= 0 and y >= 0 and x < n and y < m:
#         return True
#     return False


# def check_insert(x, y):
#     for i in range(4):
#         nx1, nx2, nx3 = x+dx[i][0], x+dx[i][1], x+dx[i][2]
#         ny1, ny2, ny3 = y+dy[i][0], y+dy[i][1], y+dy[i][2]

#         if check_range(nx1, ny1) and check_range(nx2, ny2) and check_range(nx3, ny3):
#             if visited[nx1][ny1] == True and visited[nx2][ny2] == True and visited[nx3][ny3] == True:
#                 return False
#     return True


# def back(cnt, visited, s):
#     if len(s) == cnt:
#         result.add(tuple(sum(visited, [])))
#         return

#     for i in range(n):
#         for j in range(m):
#             if visited[i][j] == False and check_insert(i, j):
#                 visited[i][j] = True
#                 s.append((i, j))
#                 back(cnt, visited, s)
#                 visited[i][j] = False
#                 s.pop()


# visited = [[False]*m for _ in range(n)]
# result = 0
# back(0,0)

# print(result)
n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
count = 0


def dfs(x, y):
    global count
    # 종료 조건
    if (x, y) == (n + 1, 1):
        count += 1
        return
    if y == m:
        nx, ny = x+1, 1
    else:
        nx, ny = x, y+1
    # x, y에 네모를 놓지 않은 경우
    dfs(nx, ny)
    # x, y에 네모를 놓을 수 있고 놓는 경우
    print("x :", x, "y :", y)
    if graph[x - 1][y] == 0 or graph[x - 1][y - 1] == 0 or graph[x][y - 1] == 0:
        graph[x][y] = 1
        for p in graph:
            print(p)
        print("-------")
        dfs(nx, ny)
        graph[x][y] = 0


dfs(1, 1)
print(count)
