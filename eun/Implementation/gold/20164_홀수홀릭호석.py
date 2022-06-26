from collections import Counter
from itertools import combinations
from collections import deque

INF = int(1e9)

q = deque([[list(input()), 0]])


def count(num):  # 홀수 개수 세기
    cnt = Counter(num)
    return cnt["1"]+cnt["3"]+cnt["5"]+cnt["7"]+cnt["9"]


def cut(arr, a, b):  # 3자리 이상 숫자 자르기
    temp = int("".join(arr[:a+1])) + \
        int("".join(arr[a+1:b+1]))+int("".join(arr[b+1:]))
    return list(str(temp))


res_min = INF
res_max = 0

while q:
    n, res = q.popleft()
    res += count(n)

    if len(n) == 1:  # 한 자리일 때 끝
        res_min = min(res_min, res)
        res_max = max(res_max, res)

    elif len(n) == 2:  # 각 자리숫자 더하기
        temp = int(n[0])+int(n[1])
        n = list(str(temp))
        q.append([n, res])

    else:
        for a, b in combinations(list(range(len(n)-1)), 2):  # 두 자리 combinations
            q.append([cut(n, a, b), res])

print(res_min, res_max)
