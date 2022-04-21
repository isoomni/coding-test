import sys
'''sys.stdin = open('soom/Silver/test.txt', 'r')'''
# # 필요한 동전 개수의 최솟값을 구하는 프로그램 # 그리디
# # n개 종류의 동전을 적절히 더해서 k로 만들어야 함

input = sys.stdin.readline

n, k = map(int,input().split())

data = [int(input()) for i in range(n)]
data.sort(reverse=True)
cnt = 0
for i in range(len(data)):
    if data[i] <= k:
        cnt += k // data[i]
        k = (k % data[i])

print(cnt)
