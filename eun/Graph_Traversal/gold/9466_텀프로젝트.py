# 9466 텀프로젝트
# 2022-04-11

import sys
sys.setrecursionlimit(1000001)  # 재귀 깊이 설정
input = sys.stdin.readline


def find_group(start):
    global group
    visited[start] = True

    cycle.append(start)  # cycle 리스트에 삽입

    if visited[student[start]] == True:  # 만약 다음 노드가 방문을 했다면
        if student[start] in cycle:  # 다음 노드가 사이클 안에 있다면
            # 다음 노드부터 그 이후의 값을 group 리스트에 삽입
            group += cycle[cycle.index(student[start]):]
        return
    else:
        find_group(student[start])  # 다음 노드를 방문하지 않았다면 이어서 반복


T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n
    group = []

    for i in range(1, n+1):
        if visited[i] == False:
            cycle = []
            find_group(i)

    print(n-len(group))

# 1차 시도 -> 시간초과
# import sys
# sys.setrecursionlimit(1000001)
# input = sys.stdin.readline


# def find_group(start):
#     global student, visited

#     while True:
#         visited[start] = True
#         if start == student[start]:
#             return start
#         if visited[student[start]] == True:
#             return student[start]

#         start = student[start]


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     student = [0] + list(map(int, input().split()))

#     visited = [False]*(n+1)

#     for i in range(1, n+1):
#         if visited[i] == False:
#             visited_temp = visited[:]
#             result = find_group(i)
#             if result != i:
#                 visited = visited_temp[:]

#     print(visited.count(False)-1)
