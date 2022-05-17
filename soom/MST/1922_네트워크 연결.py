import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
data.sort(key= lambda x: x[2])
parent_table = list(range(n+1)) # node+1의 테이블

def find(node): # root node 찾기
    if parent_table[node] == node:
        return node

    parent_table[node] = find(parent_table[node])
    return parent_table[node]


def union(a, b): # 합치면서 부모노드 갱신
    a = find(a)
    b = find(b)

    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b

# 사이클 없으면,
s = 0
for a, b, c in data:
    if find(a) != find(b):  # a, b의 부모노드가 다르면, 사이클이 없을 테니까 union
        union(a, b)
        s += c

print(s)