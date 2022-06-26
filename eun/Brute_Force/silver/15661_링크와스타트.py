# 방법 1-> 시간초과 .. 중복이 너무 많이 발생함
# import sys
# from itertools import permutations

# input = sys.stdin.readline
# INF = int(1e9)

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]


# def calculate(team):
#     power = 0
#     for i in range(len(team)-1):
#         for j in range(i+1, len(team)):
#             power += grid[team[i]][team[j]]+grid[team[j]][team[i]]
#     return power


# res = INF
# for choice in permutations(list(range(n))):
#     print()
#     print("choice", choice)
#     for cut in range(n-1):
#         start_team = choice[:cut+1]
#         link_team = choice[cut+1:]
#         print("start_team", start_team)
#         print("link_team", link_team)
#         res = min(res, abs(calculate(start_team)-calculate(link_team)))
# print(res)


import sys
from itertools import combinations

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def calculate(team):
    power = 0
    for i in range(len(team)-1):
        for j in range(i+1, len(team)):
            power += grid[team[i]][team[j]]+grid[team[j]][team[i]]
    return power


res = INF
people = set(range(n))
for count in range(1, n//2+1):
    choices = list(combinations(range(n), count))
    if n % 2 == 0 and n//2 == count:  # 짝수일 경우 반만
        choices = choices[:len(choices)//2]
    for choice in choices:
        # print("choice", choice)
        start_team = set(choice)
        link_team = people - start_team
        res = min(res, abs(calculate(list(start_team)) -
                  calculate(list(link_team))))
print(res)
