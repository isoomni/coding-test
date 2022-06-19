# from collections import Counter
# from itertools import permutations
# import sys
# input = sys.stdin.readline
# s = input().strip()
# t = input().strip()

# s_dict = Counter(s)
# t_dict = Counter(t)

# a_cnt = t_dict["A"] - s_dict["A"]
# b_cnt = t_dict["B"] - s_dict["B"]

# arr = ["A"]*a_cnt+["B"]*b_cnt

# orders = set(permutations(arr))


# def solution(order):
#     temp = s
#     for i in order:
#         if i == "A":
#             temp += "A"
#         else:
#             temp += "B"
#             temp = temp[::-1]
#     if temp == t:
#         return True
#     return False


# for order in orders:
#     if solution(order):
#         print(1)
#         break
# else:
#     print(0)


import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()


def solution(t):
    if t == s:
        print(1)
        exit()

    if len(t) > 0 and t[0] == "B":  # B를 제거할 수 있다면
        temp = t[1:]
        solution(temp[::-1])

    if len(t) > 0 and t[-1] == "A":  # A를 제거할 수 있다면
        solution(t[:-1])


if not solution(t):
    print(0)
else:
    print(1)
