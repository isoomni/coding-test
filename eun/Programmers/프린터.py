from collections import deque


def solution(priorities, location):

    index = deque([i for i in range(len(priorities))])  # 인덱스 데크
    priority = deque(priorities)  # 중요도 데크

    count = 0
    while index:
        idx, rank = index.popleft(), priority.popleft()

        if len(priority) == 0 or max(priority) <= rank:
            # 남은 것이 없거나, 나머지 중에 중요도가 큰 게 없을 때
            count += 1
            if idx == location:  # 찾아야 하는 위치라면
                return count  # 반환
        else:
            index.append(idx)
            priority.append(rank)

    return count


print(solution([1], 0))
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
