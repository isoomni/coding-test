# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
# 미리 인덱스에 %n연산을 적용해서 배열에 접근하자.
import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
lp, rp = 0, 0
answer = 0

while lp != n:
    rp = lp + k # rp는 lp보다 k만큼 크다
    case = set() # case로 하면 중복을 없애준다. 나중에 len해서 중복되지 않는 접시만 세어줄 때 유리하다.
    addable = True
    for i in range(lp, rp):
        i %= n # 리스트의 앞 뒤가 연결되어 있을 때 %=n 해준다.
        case.add(data[i])
        if data[i] == c: # 숫자가 쿠폰 번호와 같으면
            addable = False  # 더할 수 없다.

    cnt = len(case)
    if addable: # 쿠폰을 더할 수 있다면
        cnt += 1  # 먹을 수 있는 접시의 개수를 하나 더해준다.
    answer = max(answer, cnt)
    lp += 1 # 한칸씩 뒤에서부터 시작하도록

print(answer)