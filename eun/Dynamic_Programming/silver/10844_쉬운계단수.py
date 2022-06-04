n = int(input())

dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 한 자리일 때 각 인덱스의 숫자로 끝나는 숫자의 개수

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]  # 0은 1 다음에만 올 수 있음
    dp[i][9] = dp[i-1][8]  # 9는 8 다음에만 올 수 있음
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]  # j는 j-1, j+1 다음에 올 수 있음

print(sum(dp[n]) % 1000000000)
