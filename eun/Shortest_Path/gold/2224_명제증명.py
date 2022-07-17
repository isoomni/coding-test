import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*58 for _ in range(58)]
base_num = ord('A')
for _ in range(n):
    temp = input().strip()
    graph[ord(temp[0])-base_num][ord(temp[-1])-base_num] = 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if graph[i][k]+graph[k][j] == 2:
                graph[i][j] = 1
res = []
for i in range(58):
    for j in range(58):
        if i == j:
            continue
        if graph[i][j] == 1:
            res.append(str(chr(i+base_num)) + " => " + str(chr(j+base_num)))
print(len(res))
for r in res:
    print(r)
