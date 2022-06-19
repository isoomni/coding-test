# import sys
# from collections import deque

# input = sys.stdin.readline

# n = int(input())

# arr = [list(map(int, input().split())) for _ in range(n)]
# arr.sort(key=lambda x: (x[0], -(x[1]-x[0])))
# table = [[0]*365 for _ in range(n)]


# def solution(start, end):
#     idx = 0
#     while True:
#         if table[idx][start] == 0 and table[idx][end] == 0:
#             table[idx][start:end+1] = [1]*(end-start+1)
#             break
#         idx += 1


# for start, end in arr:
#     solution(start-1, end-1)

# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, 1, -1, 1, -1]


# def bfs(i, j):
#     temp = [(i, j)]
#     q = deque([(i, j)])
#     table[i][j] = 0

#     while q:
#         x, y = q.popleft()

#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if nx >= 0 and ny >= 0 and nx < n and ny < 356 and table[nx][ny] == 1:
#                 table[nx][ny] = 0
#                 q.append((nx, ny))
#                 temp.append((nx, ny))

#     temp1 = sorted(temp, key=lambda x: x[0])
#     temp2 = sorted(temp, key=lambda x: x[1])

#     return (temp2[-1][1]-temp2[0][1]+1)*(temp1[-1][0]-temp[0][0]+1)


# res = 0
# for i in range(n):
#     if sum(table[i]) == 0:
#         continue
#     for j in range(365):
#         if table[i][j] == 1:
#             res += bfs(i, j)
# print(res)


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], -(x[1]-x[0])))
table = [0]*367

for start, end in arr:
    for i in range(start, end+1):
        table[i] += 1

res = 0
left = 1
for right in range(1, 367):
    if table[left] == 0:
        left = right
    else:
        if table[right] == 0:
            res += max(table[left:right])*(right-left)
            left = right
print(res)

# right가 0일 때 res에 더하므로 table을 365보다 1개 크게했다.
