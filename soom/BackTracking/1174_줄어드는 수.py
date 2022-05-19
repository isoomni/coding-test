# 백트래킹 문제 = dfs + 조건문

# 두 자리 수부터 자리마다 조합되면서 비교했을 때 줄어들면 cnt
# 첫 번째 줄어드는 수는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52, 53, 54, 60, 61
# 210, 310, 320, 321
# str으로 split 해서 int로 바꿔서 비교

import sys
input = sys.stdin.readline
n = int(input())
# 백트래킹을 이용한 문제 풀이
def bt(cur):
    answer.append(int(cur))
    for j in range(0, int(cur[-1])):  # 현재 숫자의 끝자리보다 낮은 숫자들만 그 다음 자리수에 추가한다.
        bt(cur + str(j))


if n > 1023:  # 갯수가 1023개인듯... 0 부터 9876543210 까지 이므로 얼마 안나옴
    print(-1)
else:
    answer = []
    for i in range(10):  # 맨 앞자리가 0, 1, ,... , 9
        bt(str(i))

    print(sorted(answer)[n - 1])


# num = 0
# cnt = 0
# flag = True # 숫자가 줄어듬
# while True:
#     data = list(str(num))
#     for i in range(1, len(data)):
#
#         if int(data[i-1]) > int(data[i]):
#             continue
#         else:
#             flag = False # 숫자가 줄어들지 않음
#             break
#
#     if flag == True:
#         cnt += 1
#     if cnt == n:
#         break
#
#     num += 1
#
# print(num)