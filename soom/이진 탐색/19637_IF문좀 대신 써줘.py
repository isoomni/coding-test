import sys
input = sys.stdin.readline

n, m = map(int, input().split())
power = [tuple(input().split()) for _ in range(n)] # power[i][1]만 int로 바꾸는 법 알고 싶다....

for _ in range(m):
    data = int(input())
    start, end = 0, len(power)-1
    res = 0
    while start <= end:
        mid = (start+end)//2 # 조정
        if int(power[mid][1]) >= data: # 캐릭터의 전투력보다 mid의 전투력이 높으면 안됨
            end = mid-1 # 조정
            res = mid # 조정
        else:
            start = mid+1
    print(power[res][0])

# 시간 초과
# for _ in range(m):
#     data = int(input())
#     for j in range(n):
#         if data <= int(power[j][1]):
#             print(power[j][0])
#             break




