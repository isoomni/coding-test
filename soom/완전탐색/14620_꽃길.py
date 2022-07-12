# 백트래킹(backtracking)이란? : 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법을 말합니다.
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)  # 최대 재귀 횟수를 늘려주는 방법

n = int(stdin.readline())
arr = []
res = [int(1e9)]  # 1e9 = 1*109 = 1000000000, 2e9 = 2*109 = 2000000000 특히, 2e9는 int 범위내에서 무한대 값을 나타내기 위해 사용하는 경우가 많다.
visited = set()
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))


def solve(cnt, cost, visited):
    if cnt == 3:
        res[0] = min(res[0], cost)

    else:
        for i in range(1, n - 1):  # 씨앗을 심을 수 있는 곳은 (1,1)부터 (n-1, n-1)
            for j in range(1, n - 1):
                temp_visit = set()
                temp_visit.add((i, j))
                tf = 1
                temp = arr[i][j]
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if -1 < nx < n and -1 < ny < n and (nx, ny) not in visited:
                        temp += arr[nx][ny]  # 꽃잎 땅 가격을 temp에 하나씩 추가해본다.
                        temp_visit.add((nx, ny)) # 꽃잎들을 temp에 하나씩 추가해본다.

                    else:
                        tf = 0  # 꽃잎이 하나라도 잘 안됐으면 tf를 0으로 만들어서
                        break

                if tf and temp_visit: # 실제로 visit할 수 없게 했을 것
                    visited.update(temp_visit)  # 씨앗을 심은 부분을 기준으로 상하좌우의 좌표를 visited 집합 자료형에 넣어준다.
                    solve(cnt + 1, cost + temp, visited)  # solve(심은 씨앗의 갯수, 화단을 빌리는 비용, 꽃잎이 피어 심을 수 없는 구역들)에 심은 씨앗의 개수를 하나씩 늘려준다.
                    visited -= temp_visit # 방금 temp는 res cost를 더 작아지게 하지 못했음. 그러므로 지운다.


solve(0, 0, visited)
print(*res)