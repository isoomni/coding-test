INF = int(1e9)

n = int(input())
arr = list(map(int, input().split()))

dp = [0]+[INF]*(n-1)
for i in range(1, n):
    for j in range(0, i):
        print((i-j)*(1+abs(arr[i]-arr[j])))
        print(dp[j])
        print()
        # i 번째 돌 이전에 나올 수 있는 값 중에 큰 값
        power = max((i-j)*(1+abs(arr[i]-arr[j])), dp[j])
        # i에 들어갈 값은, i에 있던 값과 i 이전에 나올 수 있는 값 중에 작은 값
        dp[i] = min(dp[i], power)

print(dp[-1])
