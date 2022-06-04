tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(2)]

    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

    if n > 1:
        # dp[0][1], dp[1][1]은 대각선 더하는 게 최대값.
        dp[0][1], dp[1][1] = dp[1][0]+arr[0][1], dp[0][0]+arr[1][1]

    # dp[0][i]는 대각선(i-1)에서 떼거나, i-2에서 뗄 때의 최댓값
    # i-2는 위아래 모두 선택 가능.
    for i in range(2, n):
        dp[0][i] = max(dp[0][i-2], dp[1][i-2], dp[1][i-1])+arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[1][i-2], dp[0][i-1])+arr[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))
