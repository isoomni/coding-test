n = int(input())
# 재귀 - 6줄씩이 한세트
stars = [[' '] * 2 * n for _ in range(n)] # 24줄, 48 2차원배열
def recursion(i, j, size):
    if size == 3:  # size가  3이 되면,
        stars[i][j] = '*' # 첫줄
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*" # 둘째줄
        for k in range(-2, 3): #셋째줄
            stars[i + 2][j - k] = "*"
            print(stars)

    else:
        newSize = size // 2  # size가  3이 될 때까지 재귀
        recursion(i, j, newSize)
        # 밑에 세트 좌우
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)


recursion(0, n - 1, n)
for star in stars:
    print("".join(star)) # 배열 -> string