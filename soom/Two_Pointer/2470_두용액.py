import sys
from math import inf
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
# [-2 4 -99 -1 98]
# two pointer - start, end
data.sort() # sort를 해서 더한 값이 점점 작아지도록! -> 이게 없어서 모두 비교해야 했다,..
start = 0
end = len(data)-1
answer = inf
while start < end:
    if abs(answer) > abs(data[start] + data[end]):  # 갱신
        answer = data[start] + data[end]
        answer_start = data[start]
        answer_end = data[end]
        if answer == 0:
            break

    if data[start] + data[end] < 0:
        start += 1
    else:
        end -= 1

print(answer_start, answer_end)



'''
# 일반 탐색 -> 시간초과
temp_a = 0
temp_b = 0
temp = inf
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if abs(temp) < abs(data[i]+data[j]):
            continue
        else:
            temp = data[i]+data[j]
            temp_a = data[i]
            temp_b = data[j]
print(temp_a, temp_b)

'''