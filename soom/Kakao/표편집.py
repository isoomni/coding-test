def solution(n, k, cmd):
    table = {x: [x-1, x+1] for x in range(n)}
    answer = ['O' for _ in range(n)]
    deleted = []
    for c in cmd:
        if len(c) > 1:
            c, x = c.split()
        if c == 'U':
            for _ in range(int(x)):
                k = table[k][0]
        elif c == 'D':
            for _ in range(int(x)):
                k = table[k][1]
        elif c == 'C':
            before, after = table[k]
            deleted.append((before, after, k))
            answer[k] = 'X'
            # 만약 삭제한 값이 첫값이거나 마지막 값이면 index를 하나 올려주거나 줄여준다.
            if before == -1:
                table[after][0] = before
                k = after
            elif after == n:
                table[before][1] = after
                k = before
            else:  # 그렇지 않다면 아랫행을 선택한다.
                table[before][1] = after
                table[after][0] = before
                k = after

        elif c == 'Z':
            before, after, num = deleted.pop()
            answer[num] = 'O'

            if before == -1:
                table[after][0] = num
            elif after == n:
                table[before][1] = num
            else:
                table[before][1] = num
                table[after][0] = num
    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
