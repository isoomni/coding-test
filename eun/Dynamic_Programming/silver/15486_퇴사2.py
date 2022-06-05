# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [0]*n
# for i in range(n-1, -1, -1):
#     if i+arr[i][0] > n:
#         continue
#     elif i+arr[i][0] == n:
#         dp[i] = arr[i][1]+dp[n-1]
#     else:
#         dp[i] = arr[i][1]+max(dp[i+arr[i][0]:])
# print(max(dp))

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [0]*n

# max_value = 0
# dp[arr[0][0]] = max(dp[arr[0][0]],  max_value + arr[0][1])

# for i in range(n):
#     max_value = max(dp[i], max_value)
#     if i+arr[i][0] >= n:
#         continue
#     dp[i+arr[i][0]] = max(dp[i+arr[i][0]],  max_value + arr[i][1])
# print(max(dp))

import sys
input = sys.stdin.readline
n = int(input())
t, p = [], []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    ti, pi = map(int, stdin.readline().split())
    t.append(ti)
    p.append(pi)

k = 0  # dp[:i+1] 중 최대값
for i in range(n):
    k = max(k, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(k + p[i], dp[i + t[i]])

print(max(dp))
