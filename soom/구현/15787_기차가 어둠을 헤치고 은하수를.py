import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [[0]*20 for _ in range(n)]
state = []

for i in range(m):
    data = list(map(int, input().split()))

    if data[0] == 1:   # 명령
        train[data[1]-1][data[2]-1] = 1  # 태운다
    elif data[0] == 2:   # 명령
        train[data[1]-1][data[2]-1] = 0  # 내린다
    elif data[0] == 3:   # 명령
        for j in range(19, 0, -1):
            train[data[1] - 1][j] = train[data[1] - 1][j - 1]
        train[data[1] - 1][0] = 0
    elif data[0] == 4:
        for j in range(19):
            train[data[1] - 1][j] = train[data[1] - 1][j + 1]
        train[data[1] - 1][19] = 0

cnt = 0
for i in range(n):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1

print(cnt)


# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# data = [tuple(map(int, input().split())) for _ in range(m)]
# train = [[0]*21 for _ in range(n+1)]
# visited = []
#
# for i in range(m):
#     if data[i][0] == 1:   # 명령
#         train[data[i][1]][data[i][2]] = 1  # 태운다
#     elif data[i][0] == 2:   # 명령
#         train[data[i][1]][data[i][2]] = 0  # 내린다
#     elif data[i][0] == 3:   # 명령
#         train[data[i][1]].insert(1, 0)  # 한 칸씩 뒤로
#         del train[data[i][1]][-1]
#     elif data[i][0] == 4:
#         del train[data[i][1]][1]  # 한 칸씩 뒤로
#         train[data[i][1]].insert(-1, 0)
#
# print(len(set(map(tuple, train))))