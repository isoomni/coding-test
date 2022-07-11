from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

arr = [(i, j) for j in range(1, n-1) for i in range(1, n-1)]
# 맨 가장자리는 꽃을 심어도 죽으므로, 한 줄 안쪽부터 심을 수 있다고 가정했다.
orders = list(combinations(arr, 3))  # 3가지 수 선택

# 위, 아래, 왼쪽, 오른쪽, 가운데
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
res = 3001

for order in orders:  # 만들어진 경우의 수 탐색
    # print(order)
    visited = [[False]*n for _ in range(n)]
    temp = 0
    mark = False
    for k in range(3):
        x, y = order[k][0], order[k][1]
        for i in range(5):
            nx = x+dx[i]
            ny = y+dy[i]

            if not visited[nx][ny]:  # 아직 꽃을 심지 않았다면
                temp += grid[nx][ny]  # 화단 대여비 추가
                visited[nx][ny] = True  # 꽃 심음 표시
            else:  # 꽃을 심었다면
                mark = True
                break  # 종료
        if mark:  # for문을 두 번 빠져나와야 했기에 mark 변수가 필요했다.
            break
    else:
        res = min(res, temp)

print(res)
