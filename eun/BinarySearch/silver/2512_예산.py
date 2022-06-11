n = int(input())
areas = list(map(int, input().split()))
m = int(input())

start, end = 0, max(areas)

while start <= end:
    mid = (start+end)//2

    temp = 0

    for area in areas:
        if area <= mid:
            temp += area
        else:
            temp += mid

    if temp > m:  # 예산안이 초과했다면
        end = mid-1  # 범위줄이기
    else:  # 예산안이 남는다면
        start = mid+1  # 범위늘리기

print((start+end)//2)
