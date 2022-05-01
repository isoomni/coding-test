# 20058 마법사 상어와 파이어스톰
# 2022-04-29

n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
magic = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check_edge(L, x, y):
    if x % (2**L) == 0 and y % (2**L) == 0:
        return True
    # if x%(2**L)==0 and y%(2**L)-1==0:
    #     return True
    # if x%(2**L)-1==0 and y%(2**L)-1==0:
    #     return True
    # if x%(2**L)-1==0 and y%(2**L)==0:
    #     return True
    return False


def turn(L, a, b):
    x, y = a, b
    for i in range(L):
        if x > y:
            break
        grid[x][y], grid[x][y+(2**L)-1], grid[x+(2**L)-1][y+(2**L)-1], grid[x+(2**L)-1][y] = grid[x+(
            2**L)-1][y], grid[x][y], grid[x][y+(2**L)-1], grid[x+(2**L)-1][y+(2**L)-1]
        x += 1
        y += 1

        temp = [grid[i][0] for i in range(x+1, x+2**L-1)]

        # 아래 -> 왼쪽
        index_x = x+(2**L)-1
        index_y = y+(2**L)-2
        target_x = index_x-1
        target_y = index_y-(2**L-2)
        while index_y > y+(2**L)-1:
            grid[target_x][target_y] = grid[index_x][index_y]
            target_x -= 1
            index_y -= 1

        # 오른쪽 -> 아래
        index_x = x+1
        index_y = y+(2**L)-1
        target_x = index_x+(2**L-2)
        target_y = index_y-(2**L-2)
        while index_x > x+(2**L)-1:
            grid[target_x][target_y] = grid[index_x][index_y]
            target_y -= 1
            index_x += 1

        # 위 -> 오른쪽
        index_x = x
        index_y = y+1
        target_x = x+1
        target_y = y+(2**L)-1
        while index_y > y+(2**L)-1:
            grid[target_x][target_y] = grid[index_x][index_y]
            target_x += 1
            index_y += 1

        # 오르쪽 -> 위
        target_x = x
        target_y = y+1
        for index in range(len(temp)):
            grid[target_x][target_y] = temp[index]
            target_y += 1


def solution(L):

    for x in range(2**n):
        for y in range(2**n):
            if check_edge(L, x, y):
                turn(L, x, y)
                print("--------------")
                print(x, y)
                for i in range(len(grid)):
                    print(grid[i])
                print("---------------")


for L in magic:
    solution(L)
