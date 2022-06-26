# 1차원 배열만 이용하여 해당 날짜에 일정이 몇개 있는지 넣어준다. 이 개수는 row의 개수가 된다.

import sys
input = sys.stdin.readline

n = int(input())

calendar = [0] * 366

for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        calendar[i] += 1

row = 0
col = 0
ans = 0
for i in range(366):
    if calendar[i] != 0:
        row = max(row, calendar[i])
        col += 1
    else:
        ans += row * col
        row = 0
        col = 0
ans += row * col
print(ans)