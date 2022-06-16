#정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())

start, end = 0, max(data)

if sum(data) <= m: # 바로 나누기
    print(max(data)) # 그냥 바로 제일 큰 값 출력
else:
    while start <= end:

        if sum(data) <= m:
            print(max(data))
            break
        else:
            for i in range(n):
                if data[i] > end:
                    data[i] -= 1
        end -= 1
# 10
# 1 1 1 1 11 11 11 11 11 100
# 100