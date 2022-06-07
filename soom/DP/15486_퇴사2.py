import sys
input = sys.stdin.readline

N = int(input())

T, P = [], []
dp = [0] * (N+1)
for _ in range(N):
    x, y = map(int, input().split())
    T.append(x)
    P.append(y)

for i in range(0, N):
    if T[i] <= N - i: # 범위 안에 있으면
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])   # * dp[i] + P[i] = i번째 날까지의 최대 금액에 i번째 맡은 일이 끝나는 날 받게 될 돈을 더한 것

    # 그 전 날꺼가 그 다음 날꺼보다 크면, 그 전날꺼를 그 다음 날에 저장
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[N])



# n = int(input())
# data = [tuple(map(int, input().split())) for i in range(1, n+1)]
# a = [(0,0)]
# data = a+data
# print(a+data)
#
# maximum = 0
# for i in range(1, len(data)):
#     j = i
#     flag = i
#     count = 0
#     while True:
#         if flag == 1:
#             flag += data[j][0]
#             count += data[j][1]
#             j = flag
#         elif flag + data[j][0] < n+1 and flag + data[j+1][0] < n+1 and data[j][0] > data[j+1][0] :
#             flag += data[j][0]
#             count += data[j][1]
#             j = flag
#         elif flag + data[j][0] < n + 1 and flag + data[j + 1][0] < n + 1 and data[j][0] < data[j + 1][0]:
#             flag += data[j][0] + 1
#             count += data[j+1][1]
#             j = flag
#         elif flag + data[j][0] == n+1:
#             count += data[j][1]
#             break
#         elif flag + data[j+1][0] == n+1:
#             count += data[j+1][1]
#             break
#         else: break
#     maximum = max(count, maximum)
# print(maximum)