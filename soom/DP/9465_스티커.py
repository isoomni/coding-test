'''
상하좌우 사용할 수 없음
0,0에서 시작하거나
1,0에서 시작하거나
두 경우 밖에 없다.
'''

import sys
input = sys.stdin.readline
t = int(input())
visited = []

for _ in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]

    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]

    for i in range(1, n):
        if i == 1:
            dp[0][i] = dp[0][i-1] + data[0][i]
            dp[1][i] = dp[0][i-1] + data[1][i]
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + data[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + data[1][i]
    print(max(dp[0][-1], dp[1][-1]))




