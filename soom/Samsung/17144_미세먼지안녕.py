# 공기청정기가 있거나, 칸이 없으면 확산이 일어나지 않는다.
# 확산되는 칸이 같거나, 이미 먼지가 있던 공간에 먼지가 확산되면 미세먼지가 더해진다.
# A/5 만큼 확산된다.
# 확산 후 남은 미세먼지 양은 A-(A/5)X(확산된 방향의 개수) 이다.

# 공기청정기 바람이 불면 한 칸씩 이동
# 공기청정기로 들어간 먼지는 사라짐
# T초 후 방에 남아있는 미세먼지의 양을 모두 더한다.

# 3시간 소요

import sys
from collections import deque
sys.stdin = open('soom/Samsung/17144.txt', 'r')
r, c, t = map(int, input().split())
data = [list(map(int, input().split())) for i in range(r)]
print(data)
# [[0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 3, 0, 0, 8], [-1, 0, 5, 0, 0, 0, 22, 0], [-1, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 10, 43, 0], [0, 0, 5, 0, 15, 0, 0, 0], [0, 0, 40, 0, 0, 0, 20, 0]]

# 공기청정기 위치
air_cleaner = [(i, j) for i in range(r) for j in range(c) if data[i][j]==-1]
# [(2, 0), (3, 0)]

dx = [-1,0,0,1]  # 좌하상우
dy = [0,-1,1,0]

# 확산하기
def spread(r,c,data):
    q = deque() # 갱신되어야 할 ((좌표), 먼지값) 큐
    result =  [[0]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            # 확산된 방향의 개수
            spread_direct_num = 0
            # 현재 노드
            if data[i][j] != 0 and data[i][j] != -1:  # 먼지가 있는 경우에, 그리고 공기청정기도 없는 구역일 경우에
                # 사방향 확인
                for k in range(4): # 방향 움직임
                    nx = i+dx[k] 
                    ny = j+dy[k]
                    if nx >= 0 and ny >= 0 and nx < r and ny < c and (nx, ny) not in air_cleaner:   # 먼지가 이동한 위치가 확산 가능한 위치라면,
                        # q에 확산할 위치, 확산할 먼지양 넣고, '확산된 방향의 개수 +1'
                        q.append([(nx, ny), data[i][j]//5])
                        spread_direct_num += 1
                # 확산을 끝내고 해당위치(i,j)에 남은 먼지의 양을 q에 넣음
                # ((i, j), 남은 먼지 양)
                result[i][j] = data[i][j]-(data[i][j]//5)*(spread_direct_num)
    print(q)
    print('result',result) # 이 결과를 최종적으로 한번에 갱신해줘야 함(바로바로 갱신해주지 않은 이유는 갱신하면 다음 계산값이 달라지기 때문에)

    for i in range(len(q)):
        result[q[i][0][0]][q[i][0][1]] += q[i][1] 
    # print('result',result)  # 회전 완성!
    return result


# 바람 회전
# 공기청정기가 어디있냐에 따라 회전하는 행이 달라진다.

# # 공기청정기 위치
# air_cleaner = [(i, j) for i in range(r) for j in range(c) if data[i][j]==-1]
# # [(2, 0), (3, 0)]
def rotaion_up(r,c,result):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_cleaner[0][0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_cleaner[0][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        result[x][y], before = before, result[x][y]
        x = nx
        y = ny

def rotaion_down(r,c,result):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_cleaner[1][0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_cleaner[1][0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        result[x][y], before = before, result[x][y]
        x = nx
        y = ny

for i in range(t):
    if i == 0:
        result = spread(r,c,data)
        rotaion_up(r,c,result)
        rotaion_down(r,c,result)
    else:
        result = spread(r,c,result)
        rotaion_up(r,c,result)
        rotaion_down(r,c,result)


answer = 0
for i in range(r):
    for j in range(c):
        if result[i][j] > 0:
            answer += result[i][j]

print(answer)