import sys
input = sys.stdin.readline
from collections import OrderedDict
n = int(input())
total = int(input())
data = list(map(int, input().split()))
desk = OrderedDict()
for i in range(len(data)):
    if data[i] not in desk:
        desk[data[i]] = 1
    elif data[i] in desk:
        desk[data[i]] += 1
    if len(desk) > n:
        # 최소값이 두개 이상이면, 가장 오래된 애를 내보냄
        if len([k for k, v in desk.items() if min(desk.values()) == v]) >=2:
            desk.popitem(last=False)
        # 최소값이 하나라면, 그 값을 내보냄
        else:
            del desk[min(desk, key=desk.get)]
ans = list(desk.keys())
print(' '.join(str(s) for s in ans))



