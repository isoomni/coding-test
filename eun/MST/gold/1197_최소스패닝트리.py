# 1197 최소스패닝트리

def find_parent(parent, x):  # 루트 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):  # 루트 노드 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(e)]
graph = sorted(graph, key=lambda x: x[2])  # 비용 적은 순으로 정렬
parent = [i for i in range(v+1)]
result = 0

for a, b, cost in graph:
    if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 발생하지 않는 경우
        union_parent(parent, a, b)  # 집합에 포함
        result += cost

print(result)
