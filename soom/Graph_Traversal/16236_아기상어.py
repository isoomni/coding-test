"""
1. 자기보다 크기가 작은 물고기를 찾는다.
2. 가장 가까운 애들부터 먹는다.
3. 지금까지 먹은 횟수가 현재 내 크기만큼 되는지 확인한다.
    만약 내 크기만큼 된다면 내 크기를 업그레이드, 먹은 횟수를 초기화한다.
4. 먹은 후, 현재 위치를 기준으로 1-3을 반복한다.

위의 1과 2에서 BFS를 사용한다.
먹고 나서는 다시 현재 위치를 기준으로 BFS 탐색을 해야하므로,
BFS Queue를 싹 비워줘야 한다.
"""

from collections import deque

n = int(input())
board = [list(map(int , input().split())) for _ in range(n)]

# 상좌우하
dxs = [-1, 0, 0, 1]  # 위아래
dys = [0, -1, 1, 0]  # 좌우

def bfs(x, y):
    q = deque([(x, y)])
    visited = set([(x, y)])

    time = 0   # 시간이 얼마나 걸렸는가
    shark = 2  # 현재 아기 상어의 크기다.
    eat = 0    # 현재 크기에서, 지금까지 먹은 물고기 수다. -> 계속 초기화
    eat_flag = False  # 현재 상태에서 물고기를 먹은 경우, 
                      # for _ in range(size) 구문을 진행하지 않기 위한 플래그다.
    answer = 0  # 최종 return 값

    while q:   
        size = len(q)
        # 위, 그리고 왼쪽을 더 우선시해서 가야하기 때문에, BFS queue를 소팅해준다.
        q = deque(sorted(q))
        for _ in range(size):
            x, y = q.popleft()
            # 현재 위치에 아기 상어보다 작은 물고기가 있어서, 이를 먹은 경우.
            # q에서 꺼낸 x, y의 값이 shark level 보다 작은 경우
            if board[x][y] != 0 and board[x][y] < shark:
                board[x][y] = 0
                eat += 1
                # 아기 상어의 크기 만큼 먹었다면, 아기 상어의 크기를 +1 해줘야한다.
                if eat == shark:
                    shark += 1
                    eat = 0    
                # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색해야 하기 때문에,
                # BFS queue 와 visited 를 초기화 해준다.
                q, visited = deque(), set([(x, y)])
                eat_flag = True
                # 먹었을 때의 시간을 저장해둔다.
                answer = time
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                    if board[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        
            # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
            if eat_flag:
                eat_flag = False
                print('반복문 끝남')
                break
        time += 1
    return answer


# 1. 초기 상어(자신)의 위치를 파악하고, 해당 자리는 판에서 비워둔다.
shark_x, shark_y = None, None
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark_x, shark_y = i, j
            board[i][j] = 0

# 2. 시작점에서 BFS 진행
print(bfs(shark_x, shark_y))