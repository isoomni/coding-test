import sys

sys.setrecursionlimit(10 ** 7)

left = dict()
right = dict()

N = int(input())
parent = [0] * (N + 1)
node_count = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c

    if b != -1:
        parent[b] = a
        node_count += 1
    if c != -1:
        parent[c] = a
        node_count += 1

# 마지막 노드 구하는 파트
last_node = 0


def traverse(node):
    global last_node
    if node == -1:
        return
    traverse(left[node])
    last_node = node
    traverse(right[node])


traverse(1)
edge_count = node_count * 2
movement = 0
# 마지막 노드까지 이동 경로의 거리 구함
while last_node != 1:
    movement += 1
    last_node = parent[last_node]
print(edge_count - movement)


# N = int(input().strip())
# tree = {}
# visited = []
#
# for n in range(N):
#     root, left, right = input().strip().split()
#     tree[root] = [left, right]
#
# def inorder(root):
#     if tree[root][0] != -1 and tree[root][0] not in visited: # 왼쪽 자식 노드가 존재하고 아직 방문하지 않았다면
#         inorder(tree[root][0]) # 왼쪽 자식 노드로 이동한다.
#     elif tree[root][1] != -1 and tree[root][1] not in visited: # 오른쪽 자식 노드가 존재하고 아직 방문하지 않았다면
#         inorder(tree[root][1]) # 오른쪽 자식 노드로 이동
#     elif tree[root][0] != -1 and tree[root][1] != -1 and tree.keys() == visited: # 현재 노드가 유사 중위 순회의 끝이라면,
#         return # 유사 중위 순회를 종료한다.
#     elif tree[root][0] != -1 and tree[root][1] != -1 and # 부모 노드가 존재한다면,
#
#
# inorder(1)
# print(tree)
