import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tag = []
for _ in range(n):
    a, b = map(str, input().split())
    tag.append((int(b), a))
users = [int(input()) for _ in range(m)]

# 어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.
# ==> lower_bound!


def solution(power):
    start, end = 0, len(tag)

    while start < end:
        mid = (start+end)//2
        if tag[mid][0] < power:
            start = mid+1
        else:
            end = mid
    print(tag[end][1])


for i in users:
    solution(i)
