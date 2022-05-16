# Kruskal 알고리즘은 간선들을 정렬해야 하기 때문에 간선이 적으면 Kruskal, 많으면 Prim을 선택한다.
'''
Kruskal
1. 간선들을 가중치에 따라 정렬
2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들 간의 사이클을 발생시키는지 확인 -> union
    - 노드들의 부모노드가 같다면 사이클 발생, 같지 않다면 사이클 발생하지 않음
3. 사이클을 발생시키지 않는다면, 최소 신장 트리에 포함시킨다. 
4. 반복 수행

Union-Find
1. 초기화
2. Union - 두 개별 집합을 하나로 합침
3. Find - 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소를 확인

Prim
1. 임의의 정점을 선택
2. 해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
3. 최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.
'''
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(e)]

# 1. 가중치에 따라 정렬
data.sort(key=lambda x: x[2])
parent_table = list(range(v+1))


# 2. 루트노드 찾기
def find(node):
    if node == parent_table[node]:
        return node # 현재 노드값과 부모 노드 값이 같으면 그 부모 노드가 루트 노드이므로 반환
    parent_table[node] = find(parent_table[node])  # 현재 노드값과 부모 노드 값이 다르면, 루트 노드를 찾을 때까지 find 함수 재귀 호출
    return parent_table[node]

# 3. 두 원소가 속한 집합을 합친다. 이 때 부모노드를 갱신해준다.
def union(a, b):
    a = find(a)
    b = find(b)

    # 노드 번호가 더 큰 것의 값을 노드 번호가 더 작은 것의 값으로 바꿔 준다. '더 큰 값의 부모 노드' == '더 작은 값' 이기 때문이다.
    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b

s = 0
for a, b, c in data:
    if find(a) != find(b): # 부모노드가 다르면 사이클이 안도니까 union(최소 신장 트리에 포함)
        union(a, b)  # 사이클을 발생 시키지 않는 다면, 최소 신장 트리에 포함 시킨다.
        s += c # 사이클을 돌지 않는 간선의 가중치를 더해준다.

print(s)