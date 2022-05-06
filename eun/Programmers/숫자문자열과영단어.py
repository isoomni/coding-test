def solution(s):
    table = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
             'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    num_str = ""  # 숫자로 바꿀 문자열 저장
    answer = ""  # 정답
    for index in range(len(s)):

        if s[index].isdigit():  # 만약에 숫자면
            answer += s[index]
        else:  # 문자열이라면
            num_str += s[index]  # num_str에 더하고
            if num_str in table:  # 숫자로 바꿀 수 있는 문자열이라면
                answer += table[num_str]  # answer에 더하기
                num_str = ""  # 초기화

    return int(answer)


print(solution("one4seveneight"))  # 1478
print(solution("23four5six7"))  # 234567
print(solution("2three45sixseven"))  # 234567
print(solution("123"))  # 123
