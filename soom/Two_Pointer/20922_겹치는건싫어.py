# 최장 연속 부분 수열
# 같은 원소가 k개 이하로 들어 있는 수열의 길이를 구한다.
# 9개의 수열, 같은 원소가 2개 이하로 들어 있는 수열의 길이를 구하라.
# 3 2 5 5 6 4 4 5 7
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, 0
seq = {i:0 for i in set(data)} # seq 를 먼저 만든다. 안그러면 조건문을 너무 많이 추가해줘야 했다..논리 꼬임(기억!)
answer = 0
while end < n:
    if seq[data[end]] < k:
        seq[data[end]] += 1
        end += 1
    else:
        seq[data[start]] -= 1
        start += 1
    answer = max(answer, end - start)
print(answer)