s = input()
used = [False]*len(s)


def view():  # 출력하는 함수
    answer = ""
    for i in range(len(used)):
        if used[i]:
            answer += s[i]
    print(answer)


# arr은 슬라이스 한 리스트, start_idx는 s 기준 인덱스 // 따라서 used에 표시해 줄 때에는 start_idx + min_idx를 해주어야 한다.
def solution(arr, start_idx):
    global answer
    if not arr:
        return
    min_idx = 0
    min_value = "a"

    for i in range(len(arr)):
        if not used[start_idx+i] and min_value > arr[i]:
            min_idx = i
            min_value = arr[i]

    used[start_idx+min_idx] = True
    view()  # 출력
    solution(arr[min_idx+1:], start_idx+min_idx+1)  # 최소 문자열 다음부터
    solution(arr[:min_idx], start_idx)  # 최소 문자열 이전 탐색


solution(list(s)[:], 0)
