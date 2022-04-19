# deque로 선언 - 좌우로 빼고 넣어야 함
# priorities의 원래 인덱스를 관리해주기 위해 [(),(),(),()...]이렇게 딕셔너리로 관리
# printer 리스트에 최종 출력할 순서를 관리
# location을 딕셔너리 key값으로 찾아서 printer idx를 출력
# 40점
from collections import deque
priorities = [1, 1, 3, 1, 3, 1, 3]
location = 3
def solution(priorities, location):
    temp = []
    answer = 0
    for i in range(len(priorities)):
        temp.append((i,priorities[i]))
        q = deque(temp)
    print(q)
    
    pre = []
    nxt = []
    for i in range(len(q)):
        pl = q.popleft()
        for j in range(len(q)):
            print('popleft한 수, 비교 수', pl[1], q[j][1])
            if pl[1] < q[j][1]:
                pre.append(pl)
                print('pre에 넣었음', pre)
                break
        if pl not in pre:
            nxt.append(pl)
            print('next에 넣었음',nxt)
    q = nxt + pre
    print(q)
    
    for i in range(len(q)):
        if q[i][0] == location:
            return i+1

print(solution(priorities, location))