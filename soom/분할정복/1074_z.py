import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

ans = 0

while N != 0:

    N -= 1
    # 하나의 사분면에서만 조사해도 된다.
    # 1사분면
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0

    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)

    # 3사분면
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)

    # 4사분면
    else: # 쪼개기
        ans += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)  # 가로세로 네칸씩 줄어듬
        c -= (2 ** N)

print(ans)