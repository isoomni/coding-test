# 15684 사다리 조작
# 2022-04-22

from itertools import combinations
import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())

grid = [[0]*(H+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    grid[b][a] = 1

empty_list = []

# 사다리를 놓을 수 있는지 확인하고, 넣을 수 있으면 empty_list에 append
for i in range(1, N+1):
    for j in range(1, H+1):
        if grid[i][j] == 0:  # 해당 칸이 비어있고
            if i == 1:  # 첫 번째 세로줄 일 때
                if grid[i+1][j] == 0:  # 오른쪽에 다리가 없어야함
                    empty_list.append((i, j))
            elif i != N:  # 맨 끝 줄이 아닐 때
                if grid[i+1][j] == 0 and grid[i-1][j] == 0:  # 좌우로 다리가 없어야 함
                    empty_list.append((i, j))


def find(start):
    height = 0
    while True:
        if height == H:  # 맨 마지막에 도달하면 멈춤
            break
        for i in range(1, H+1):
            if i <= height:  # 아래로 탐색해야 함.
                continue
            if grid[start][i] == 1 and start < N:  # 오른 쪽에 다리가 있을 때
                start += 1
                height = i
                break
            elif grid[start-1][i] == 1 and start > 1:  # 왼쪽에 다리가 있을 때
                start -= 1
                height = i
                break

            height = i

    return start


def solution():
    # 다리를 놓지 않았을 때
    for i in range(1, N+1):
        result = find(i)
        if result != i:
            break
    else:
        return 0

    # 다리를 하나 놓았을 때
    for empty in empty_list:
        mark = True
        grid[empty[0]][empty[1]] = 1
        for i in range(1, N+1):
            result = find(i)
            if result != i:
                grid[empty[0]][empty[1]] = 0
                mark = False
                break
        if mark:
            return 1

    # 다리를 두 개 놓았을 때
    # 경우의 수는 조합으로 구함
    two = list(combinations(empty_list, 2))
    for empty in two:
        mark = True
        if (abs(empty[0][0]-empty[0][1]) == 1) and empty[0][1] == empty[1][1]:
            # 고른 두 개의 다리가 이어져 있다면 continue
            continue
        grid[empty[0][0]][empty[0][1]] = 1
        grid[empty[1][0]][empty[1][1]] = 1
        for i in range(1, N+1):
            result = find(i)
            if result != i:
                grid[empty[0][0]][empty[0][1]] = 0
                grid[empty[1][0]][empty[1][1]] = 0
                mark = False
                break
        if mark:
            return 2

    # 다리를 세 개 놓았을 때
    # 경우의 수는 조합으로 구함
    three = list(combinations(empty_list, 3))
    for empty in three:
        mark = True
        if ((abs(empty[0][0]-empty[1][0]) == 1) and empty[0][1] == empty[1][1]) or ((abs(empty[1][0]-empty[2][0]) == 1) and empty[1][1] == empty[2][1]) or ((abs(empty[0][0]-empty[2][0]) == 1) and empty[0][1] == empty[2][1]):
            # 고른 세 개의 다리 중 두 개의 다리가 붙어있다면  continue
            continue
        grid[empty[0][0]][empty[0][1]] = 1
        grid[empty[1][0]][empty[1][1]] = 1
        grid[empty[2][0]][empty[2][1]] = 1
        for i in range(1, N+1):
            result = find(i)
            if result != i:
                grid[empty[0][0]][empty[0][1]] = 0
                grid[empty[1][0]][empty[1][1]] = 0
                grid[empty[2][0]][empty[2][1]] = 0
                mark = False
                break
        if mark:
            return 3

    return -1


print(solution())
