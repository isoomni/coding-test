# result = [[0, 1], [2, 3]]


# def solution(result):
#     start = result[-1][-1]+1
#     temp = []
#     for i in range(len(result)*2):
#         if i // len(result) == 0:
#             temp.append(result[i]+list(range(start, start+2)))
#         else:
#             temp.append([start, start+1, start+4, start+5])
#         start += 2
#     return temp


# n, x, y = map(int, input().split())
# for _ in range(1, n):
#     result = solution(result)
# print(result[x][y])
n, r, c = map(int, input().split())
num = -1


def recursive(x, y, N):
    global num

    if N == 2:
        for i in range(x, x + N):
            for j in range(y, y + N):
                num += 1
                if i == r and j == c:
                    print(num)
                    exit(0)
        return

    if not (x <= r < x + N and y <= c < y + N):  # 해당 범위에 없다면
        num += N * N
        return

    for i in range(x, x + N, N // 2):
        for j in range(y, y + N, N // 2):
            print(i, j)
            recursive(i, j, N // 2)


recursive(0, 0, 2 ** n)
