import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [[0]*21 for _ in range(n+1)]
commends = [list(map(int, input().split())) for _ in range(m)]
res = set()

for commend in commends:
    if commend[0] == 1:
        t, s = commend[1], commend[2]
        if train[t][s] == 0:
            train[t][s] = 1

    elif commend[0] == 2:
        t, s = commend[1], commend[2]
        if train[t][s] == 1:
            train[t][s] = 0

    elif commend[0] == 3:  # 한 칸씩 뒤로
        t = commend[1]
        train[t] = [0]+train[t][:-1]

    else:  # 한 칸씩 앞으로
        t = commend[1]
        train[t] = [0]+train[t][2:]+[0]

for i in range(1, n+1):
    res.add(tuple(train[i]))

print(len(res))
