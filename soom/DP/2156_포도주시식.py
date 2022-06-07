import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = wine[i]
    elif i == 1:
        dp[i] = wine[i-1] + wine[i]
    elif i == 2:
        dp[i] = max(dp[i-1], wine[i-2] + wine[i], wine[i-1] + wine[i])
    else:
        dp[i] = max((dp[i-1]), (dp[i-2] + wine[i]), (dp[i-3] + wine[i-1] + wine[i]))

print(dp[-1])
