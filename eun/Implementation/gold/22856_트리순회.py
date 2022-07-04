import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = {}
for _ in range(n):
    now, left, right = map(int, input().split())
    tree[now] = [left, right]
visited = [False]*(n+1)
count = 0

inorder_list = []


def inorder(tree, node):  # 중위 순회 LMR
    if node != -1:
        inorder(tree, tree[node][0])
        inorder_list.append(node)
        inorder(tree, tree[node][1])


arr = []


def solution(now):
    global count
    if now != -1:
        left, right = tree[now]
        visited[now] = True
        count += 1
        arr.append(now)
        if not visited[left]:
            solution(left)

        if not (tree[now][0] == -1 and tree[now][1] == -1):
            count += 1
            arr.append(now)
        if not visited[right]:
            solution(right)
    if now == inorder_list[-1]:
        print(count-1)
        exit(0)


inorder(tree, 1)
solution(1)
print(count-1)
