from itertools import permutations

expression = input()


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(exp, op):
    array = []
    tmp = ""
    for i in exp:
        if i.isdigit():  # 숫자라면, temp에 숫자를 이어준다.
            tmp += i
        else:
            array.append(tmp) # i가 숫자가 아니라면 만들어 둔 연결된 숫자들을 array에 넣어준다.
            array.append(i) # 연산자를 array에 넣어준다.
            tmp = ""
    array.append(tmp) # 마지막 tmp까지 넣어준다.

    for o in op: # op은 solution 함수에서 만들었던 연산자 조합이다.
        stack = []
        while len(array) != 0:
            tmp = array.pop(0) # array의 가장 앞
            if tmp == o:  # array에서 뽑아 온 것과 연산자가 같으면
                stack.append(operation(stack.pop(), array.pop(0), o)) #stack에 마지막으로 들어온 값과, array 가장 앞에 남은 값, 연산자를 operation 함수로 보내서 연산한다.
            else:
                stack.append(tmp) # array에서 뽑아 온 것과 연산자가 다르면(숫자이거나 다른 연산자), stack에 넣어준다.
        array = stack  # array에 stack을 넣어서 계산된 값을 갱신한다.

    return abs(int(array[0]))  # 절댓값을 취한다.


def solution(expression):
    op = ['+', '-', '*']  # 연산자 선언
    op = list(permutations(op, 3))  # 연산자를 조합하여 리스트를 만든다. 순서를 가질 수 있도록
    result = []
    for i in op: # 연산자 우선순위만큼 loop를 돈다.
        result.append(calculate(expression, i))
    return max(result) # 최대를 출력한다.


print(solution(expression))
