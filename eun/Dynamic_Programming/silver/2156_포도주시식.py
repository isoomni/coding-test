# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [0] + [int(input()) for _ in range(n)]

# dp = [[0, 0, 0] for _ in range(n+1)]

# if n < 3:
#     print(sum(arr))
# else:

#     dp[1][1] = arr[1]

#     if arr[2] != 0:
#         dp[2][1] = arr[2]
#         dp[2][2] = arr[1]+arr[2]
#     else:
#         dp[2][0] = arr[1]

#     for i in range(3, n+1):
#         if arr[i] == 0:
#             dp[i][0] = max(dp[i-1])
#         else:
#             dp[i][0] = dp[i-1][0]
#             dp[i][1] = max(dp[i-1][0], dp[i-2][1], dp[i-2][2])+arr[i]
#             dp[i][2] = dp[i-1][1]+arr[i]

#     result = 0
#     for i in range(1, n+1):
#         temp = max(dp[i])
#         if result < temp:
#             result = temp
#     print(result)


import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

dp = [0]*(n+1)

dp[1] = arr[1]
if n > 1:
    dp[2] = arr[1]+arr[2]
for i in range(3, n+1):
    # i 안 마심
    # i 마시고, i-1 안 마시고, i-2 마심
    # i 마시고, i-1 마시고, i-2 안 마심
    dp[i] = max(dp[i-1], arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3])


print(dp[n])
