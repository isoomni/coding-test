import sys
input = sys.stdin.readline

n, k = map(int, input().split())

si = list(map(int, input().split()))
di = list(map(int, input().split()))

for _ in range(k):
    temp = [0]*n
    for i in range(n):
        temp[di[i]-1] = si[i]
    si = temp[:]

print(*si)
