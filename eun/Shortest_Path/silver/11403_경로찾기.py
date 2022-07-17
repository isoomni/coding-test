import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k]+arr[k][j] == 2:  # 갈 수 있다면
                arr[i][j] = 1
for a in arr:
    print(*a)
