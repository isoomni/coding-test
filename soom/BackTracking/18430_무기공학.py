import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(x, y, i):
    for p in range(2):
        nx, ny = x+dx[(i+p) % 4], y+dy[(i+p) % 4]
        if not (0 <= nx < n and 0 <= ny < m):
            return False
        if visit[nx][ny]:
            return False
    return True

def solve(idx, res):
    global ans
    if idx == n*m:
        ans = max(ans, res)
        return
    x, y = idx//m, idx % m

    if not visit[x][y]:
        for i in range(4):
            if check(x, y, i):
                x1, y1 = x+dx[i], y+dy[i]
                x2, y2 = x + dx[(i+1) % 4], y+dy[(i+1) % 4]
                visit[x][y] = visit[x1][y1] = visit[x2][y2] = True
                solve(idx+1, res+2*a[x][y]+a[x1][y1]+a[x2][y2])
                visit[x][y] = visit[x1][y1] = visit[x2][y2] = False
    solve(idx+1, res)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
ans = 0
solve(0, 0)
print(ans)