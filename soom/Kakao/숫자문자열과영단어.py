s = input()


def solution(s):
    mapping = [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'),
               (8, 'eight'), (9, 'nine')]
    answer = ''
    flag = 0
    for i in range(1,len(s)+1):
        if not (s[flag:flag + 1]).isdigit():
            for j in range(len(mapping)):
                if s[flag:i] == mapping[j][1]:
                    answer += str(mapping[j][0])
                    flag = i
        else:
            answer += str(s[flag:i])
            flag += 1
    return answer


print(solution(s))
