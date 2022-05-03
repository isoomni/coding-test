# 상어중학교
# 2022-05-02
import sys
sys.stdin = open('eun/input/21609.txt', 'r')
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 블록 찾기 -> dfs


def find_block(x, y, num):
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < n:  # 범위 체크
            if (grid[nx][ny] == num and visited[nx][ny] == False) or (grid[nx][ny] == 0 and (nx, ny) not in rainbow):
                # 숫자가 같으며 아직 방문하지 않았을 때
                # 혹은
                # 무지개 블록일 때 -> 두 번 이상 방문할 수 있으므로 rainbow 리스트에서 이미 방문 한 기록이 있는지 확인
                block.append((nx, ny))
                if grid[nx][ny] == 0:
                    rainbow.append((nx, ny))  # rainbow 일 경우 append
                find_block(nx, ny, num)


# 최대 블록 찾기
def find_max(block_list):
    # block_list.sort()

    # 크기가 가장 큰 블록 찾기
    max_index = 0
    for i in range(1, len(block_list)):
        if len(block_list[max_index]) < len(block_list[i]):  # 길이가 가장 긴 것
            max_index = i
        elif len(block_list[max_index]) == len(block_list[i]):  # 길이가 같다면
            # 무지개 블럭 수가 많은 것, 같다면 인덱스 더 높은 것(이미 블록이 정렬되어 있음)
            if block_list[max_index][-1] <= block_list[i][-1]:
                max_index = i

    return max_index


# 블록 지우기
def delete_block(block):
    for i in range(len(block)-1):
        grid[block[i][0]][block[i][1]] = None

# 블록 움직이기


def move_block():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if (grid[i][j] != None and grid[i][j] != -1) and grid[i+1][j] == None:
                # 현재 index에 블록이 있고, 마로 밑에 블록이 없을 때
                index = i+1
                while index < n:  # 맨 마지막에 도달하면 종료
                    if grid[index][j] != None:
                        # 다른 블록을 만날 때 까지 반복
                        break
                    grid[index-1][j], grid[index][j] = grid[index][j], grid[index-1][j]
                    index += 1


answer = 0
while True:
    block_list = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != None and grid[i][j] > 0 and visited[i][j] == False:
                block = [(i, j)]  # 대표블록
                rainbow = []
                find_block(i, j, grid[i][j])
                if len(block) > 1:
                    # 무지개 블록의 개수를 같이 넣어줌
                    block_list.append(block+[len(rainbow)])

    if not block_list:  # 블록이 없다면 종료
        break

    max_index = find_max(block_list)  # 가장 큰 블록 찾기
    delete_block(block_list[max_index])  # 블록 삭제
    answer += (len(block_list[max_index])-1)**2  # answer

    move_block()  # 블록 중력
    grid = list(map(list, zip(*grid)))[::-1]  # 블록 90도 회전
    move_block()  # 블록 중력

print(answer)
