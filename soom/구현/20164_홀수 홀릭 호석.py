import sys
input = sys.stdin.readline

N =str(input().rstrip())
cnt = 0
min_v = 999  #각각 초기설정은 반대로
max_v = 0


def count_odd(arr):
    cnt = 0
    for i in arr:
        if int(i) % 2 == 1:   #문자열은 이와같이 for 문으로 활용가능
            cnt += 1
    return cnt


def dfs(N, cnt):

    global min_v, max_v
    cnt = cnt + count_odd(N)

    if len(N) == 1:
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return
    elif len(N) == 2:
        temp = int(N)//10 + int(N) % 10
        N = str(temp)
        dfs(N, cnt)
    else:
        for i in range(1, len(N)):
            for j in range(i+1, len(N)):

                temp = int(N[:i]) + int(N[i:j]) + int(N[j:])
                print(temp)
                dfs(str(temp), cnt)


dfs(N, 0)
print(min_v, max_v)