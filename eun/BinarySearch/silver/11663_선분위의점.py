from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
point = list(map(int, input().split()))
point.sort()


def lower_bound(p):
    start, end = 0, n  # end를 n으로 설정해야함..!!!

    while start < end:
        mid = (start+end)//2

        if point[mid] < p:
            start = mid+1
        else:  # lower_bound 이므로 같으면 줄임.
            end = mid
    return end


def upper_bound(p):
    start, end = 0, n

    while start < end:
        mid = (start+end)//2

        if point[mid] <= p:  # upperbound 이므로 같으면 늘림
            start = mid+1
        else:
            end = mid
    return end


lines = [list(map(int, input().split())) for _ in range(m)]
for a, b in lines:
    print(upper_bound(b)-lower_bound(a))  # 892ms
    # print(bisect_right(point, b)-bisect_left(point, a)) # 444ms -> 더 빠름!
