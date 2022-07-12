import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))


for _ in range(k):
    p = [0]*len(d)
    for i in range(len(d)):
        p[d[i]-1] = s[i]
    s = p[:]

print(*p)