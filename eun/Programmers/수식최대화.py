from itertools import permutations
from collections import deque
import re


def calculate(number, op_list, perm_op):

    number = deque(number)  # 계산할 숫자가 담김 데크
    op_list = deque(op_list)  # 연산자가 담긴 데크
    for op in perm_op:  # 계산 순서

        temp = []
        temp_op = []
        temp.append(number.popleft())  # temp에 넣고 시작
        while number:
            now_op = op_list.popleft()  # 다음 연산자
            next_num = number.popleft()  # 다음 숫자
            if op == now_op:  # 만약 해당 순위의 연산자라면
                num = temp.pop()  # temp에서 꺼내어 계산 후 다시 저정
                if now_op == "-":
                    temp_num = num-next_num
                elif now_op == "+":
                    temp_num = num+next_num
                else:
                    temp_num = num*next_num

                temp.append(temp_num)  # 저장
            else:  # 해당 순위의 연산자가 아니라면 그대로 append
                temp.append(next_num)
                temp_op.append(now_op)

        number = deque(temp[:])
        op_list = deque(temp_op[:])

    return int(number[0])


def solution(expression):
    op_list = []
    # *,+,- 기준으로 split // number=[100, 200, 300, 500, 20]
    number = list(map(int, re.split("[-*+]", expression)))
    for i in expression:
        if i.isdigit() == False:
            # op_list에 연산자만 담기 // op_list = ["-", "*", "-", "+"]
            op_list.append(i)

    # operation = []
    # for op in ["*", "+", "-"]: # 실제로 있는 연산자 개수 세기
    #     c = op_list.count(op)
    #     if c:
    #         operation.append(op)

    # perm_ops = list(permutations(operation, len(operation))) # 사용한 연산자를 가지고 조합 만들기

    # 어차피 없으면 연산 안되므로 모든 경우의 수 고려해도 될 것 같다.
    perm_ops = list(permutations(["+", "-", "*"], 3))
    result = 0
    for perm_op in perm_ops:  # 조합으로 만든 연산자를 차례로 계산
        r = calculate(number, op_list, perm_op)
        if abs(r) > result:
            result = abs(r)
    return result


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
