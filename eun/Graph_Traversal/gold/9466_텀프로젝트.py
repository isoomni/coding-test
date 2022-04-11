# 9466 텀프로젝트
# 2022-04-11

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


import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline


def find_group(start):
    global group
    visited[start] = True
    route.append(start)
    if visited[student[start]] == True:
        if student[start] in route:
            group += route[route.index(student[start]):]
        return

    find_group(student[start])


T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n
    group = []

    for i in range(1, n+1):
        if visited[i] == False:
            route = []
            find_group(i)

    print(n-len(group))
