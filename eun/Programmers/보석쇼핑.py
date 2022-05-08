from collections import Counter


def solution(gems):
    need = Counter(set(gems))  # 필요한 보석
    count = len(set(gems))  # 필요한 보석 개수
    left = right = start = end = 0  # left, right -> 현재 탐색 , start, end -> 정답

    for right, gem in enumerate(gems, 1):
        count -= need[gem] > 0  # 보석이 있을 때 count 감소
        need[gem] -= 1  # 보석 개수 감소

        if count == 0:  # count가 0 일 때 == 더이상 늘리지 않아도 될 때
            # 왼쪽에 불필요한 값이 있는 지 확인하고 제거. need[gems[left]]가 0이하 라는 것은 필요한 값이 여러 개 들어가 있다는 말.
            while left < right and need[gems[left]] < 0:
                need[gems[left]] += 1  # 왼쪽에 있는 보석의 개수를 늘려주고
                left += 1  # left 포인터 증가

            if not end or right-left < end-start:  # 처음이거나, 지금까지 탐색한 결과보다 짧은 길이가 나왔을 때
                start, end = left, right  # 갱신

            # 오른쪽으로 한 칸씩 옮겨서 탐색 다시하기
            need[gems[left]] += 1  # 왼쪽에 있는 보석 개수 늘리고
            count += 1  # count 다시 늘리고
            left += 1  # left 포인터 오른쪽으로 이동
    return [start+1, end]


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
