n = int(input())
result = []


def back(digit, s):
    if len(s) == digit:  # 자릿수에 도달하면
        result.append(s)  # append
        return

    for i in range(10):  # 0부터 9까지 삽입
        if not s or int(s[-1]) > i:
            s += str(i)
            back(digit, s)
            s = s[:-1]


digit = 1  # 자릿수
while len(result) < n:
    before = len(result)
    back(digit, "")
    if before == len(result):  # 탐색 전과 후의 결과가 같다면 -> 더이상 늘어나지 않음
        print(-1)
        break
    digit += 1  # 자릿수 증가
else:
    print(result[n-1])
