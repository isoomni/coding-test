import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()

def dot_min(a):  # 가장 작은 점 구하기
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if dot[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def dot_max(b):   # 가장 큰 점 구하기
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


for i in range(m):
    a, b = map(int, input().split())
    print(dot_max(b) - dot_min(a) + 1)

