from collections import deque


def solution(progresses, speeds):
    q = deque(progresses)
    s = deque(speeds)
    result = []
    while q:
        if q[0] >= 100:  # 첫 번째에 있는 기능이 배포 가능할 때
            q.popleft()
            s.popleft()
            count = 1
            while q:
                if q[0] >= 100:  # 그 다음 원소도 배포 가능한지 확인
                    q.popleft()
                    s.popleft()
                    count += 1
                else:
                    break
            result.append(count)
        else:
            for i in range(len(q)):
                q[i] += s[i]

    return result


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
