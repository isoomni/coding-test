# deque로 선언 - 좌우로 빼고 넣어야 함
# priorities의 원래 인덱스를 관리해주기 위해 [(),(),(),()...]이렇게 딕셔너리로 관리
# printer 리스트에 최종 출력할 순서를 관리
# location을 딕셔너리 key값으로 찾아서 printer idx를 출력
# 40점
from collections import deque
priorities = [1,5,2,21,6]
location = 2
from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(i, priorities[i]) for i in range(len(priorities))])
    
    result = []
    while q:
        pl = q.popleft()
        for i in range(len(q)):
            if pl[1] < q[i][1]:
                q.append(pl)
                break
        if pl not in q:
            result.append(pl)
    
    for i in range(len(result)):
        if result[i][0] == location:
            return i+1

print(solution(priorities, location))