# 문자열 압축
# 2022-04-15

def solution(s):
    result = 1000  # 최종 반환 될 문자열의 길이
    if len(s) == 1:  # 만약 문자열의 길이가 1이라면
        return 1  # 1 반환

    for i in range(1, len(s)):
        # i = 자르는 단위 수
        answer = ""
        count = 1
        for j in range(0, len(s), i):
            if j+i < len(s):  # j+i가 문자열의 길이 보다 작을 때 == 아직 탐색할 문자열이 남았을 때
                if s[j:j+i] == s[j+i:(j+i)+i]:
                    count += 1
                else:
                    if count == 1:
                        answer += s[j:j+i]
                    else:
                        answer += str(count)+s[j:j+i]

                    count = 1

            elif j+i == len(s):  # j+i가 문자열의 길이와 같을 때 == i개로 문자열이 딱 맞게 잘라질 때
                if count == 1:
                    answer += s[j:]
                else:
                    answer += str(count)+s[j-i:j]
            else:  # j+i가 문자열의 길이보다 클 때 == i개로 문자열을 자르고 남는 것이 있을 때
                answer += s[j:]

        if len(answer) < result:  # answer의 길이가 result보다 짧다면
            result = len(answer)  # 갱신

    return result


print(solution("a"))
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("acdhdh"))
