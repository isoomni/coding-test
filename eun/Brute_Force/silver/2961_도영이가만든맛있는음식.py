from itertools import combinations
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

orders = []

for i in range(1, n+1):
    orders.extend(list(combinations(list(range(n)), i)))

res = INF
for order in orders:
    sour = 1  # 곱해야 하므로 초기값 1
    bitter = 0

    for i in order:
        sour *= arr[i][0]
        bitter += arr[i][1]

    if abs(sour-bitter) < res:
        res = abs(sour-bitter)
print(res)
