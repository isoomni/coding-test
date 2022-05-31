# from collections import defaultdict

# def short(s):
#     left, right = 0, 0

#     shortest = len(s)+1

#     count = defaultdict(int)

#     while right < len(s):
#         if count[s[right]] == k-1:
#             shortest = min(shortest, right-left+1)
#             count[s[left]] -= 1
#             left += 1
#         else:
#             count[s[right]] += 1
#             right += 1

#     return shortest

# tc = int(input())

# for _ in range(tc):
#     s = input()
#     k = int(input())

#     left, right = 0, 0

#     shortest = len(s)+1
#     longest = -1

#     count = defaultdict(int)

#     while right < len(s):
#         if count[s[right]] == k-1:
#             shortest = min(shortest, right-left+1)
#             if s[left] == s[right]:
#                 longest = max(longest, right-left+1)
#             count[s[left]] -= 1
#             left += 1
#         else:
#             count[s[right]] += 1
#             right += 1

#     if shortest == len(s)+1 or longest == -1:
#         print(-1)
#     else:
#         print(shortest, longest)

from collections import defaultdict

tc = int(input())  # test case

for _ in range(tc):
    s = input()
    k = int(input())
    count = defaultdict(list)
    for idx, elem in enumerate(s):
        count[elem].append(idx)  # 각 문자의 인덱스를 리스트로 저장

    shortest, longest = len(s)+1, -1

    for key, value in count.items():
        if len(value) >= k:  # value가 k 개 이상이라면
            for i in range(k-1, len(value)):  # k개 만큼 포함해야 함.
                # "a" : [5, 8, 13]라고 할 때
                # k가 2라면 8-5, 13-8을 해아하고
                # k가 3이라면 13-5를 해야 함.
                shortest = min(shortest, value[i]-value[i-(k-1)]+1)
                longest = max(longest, value[i]-value[i-(k-1)]+1)

    if shortest == len(s)+1 or longest == -1:
        print(-1)
    else:
        print(shortest, longest)
