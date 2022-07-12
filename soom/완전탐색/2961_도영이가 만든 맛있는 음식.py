import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
res = 1e9

for i in range(1,n+1):
    combi_data = list(combinations(data, i))
    for j in range(len(combi_data)):
        sour = 1
        bitter = 0
        for k in range(i):
            sour *= combi_data[j][k][0]
            bitter += combi_data[j][k][1]
        res = min(res, abs(sour-bitter))
print(res)