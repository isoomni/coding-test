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
length = 0
while end < n:  # end 를 n을 넘어가지 않을 때까지 뒤로뒤로~
    if seq[data[end]] < k:      # 원소의 개수가 k 미만이면, ((k가 2일때,)1개면 2개로 만드는 것 가능, 이미 2개면 3개로 만들지 않는다.)
        seq[data[end]] += 1     # 원소의 개수를 하나 더하고
        end += 1                # end도 하나씩 오른쪽으로
    else:                       # 원소의 개수가 k 이상이면 그 다음부터는 end가 아니라 start를 조정한다.
        seq[data[start]] -= 1   # 원소의 개수를 하나 줄이고
        start += 1              # start 하나씩 오른쪽으로
    length = max(length, end - start)       # length는 최댓값으로
print(length)