import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

min_value = 100 * 20


def recur(target):
    if target == n:
        score() # score 함수 호출
        return

    visited[target] = True
    recur(target + 1)
    visited[target] = False
    recur(target + 1)


def score():
    global min_value

    start = 0
    link = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if visited[i] and visited[j]:
                start += data[i][j] + data[j][i]
            elif not visited[i] and not visited[j]:
                link += data[i][j] + data[j][i]

    diff = abs(start - link)

    if min_value > diff:
        min_value = diff


recur(0)

print(min_value)

