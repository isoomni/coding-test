def solution(name):
    move_right = 0
    move_left = 0
    now = 0

    for i in range(len(name)):
        if name == "A":
            continue

        if ord(name[i])-ord("A") < 14:
            move_right += ord(name[i])-ord("A")
        else:
            move_right += 26-(ord(name[i])-ord("A"))

        move_right += 1

    if ord(name[0])-ord("A") < 14:
        move_left += ord(name[0])-ord("A")
    else:
        move_left += 26-(ord(name[0])-ord("A"))

    move_left += 1

    for i in range(len(name)-1, 0, -1):
        if name == "A":
            continue

        if ord(name[i])-ord("A") < 14:
            move_left += ord(name[i])-ord("A")
        else:
            move_left += 26-(ord(name[i])-ord("A"))

        move_left += 1

    # if len(name) > 1:
    #     if name[0] == "A" or name[1] == "A":
    #         move -= 1
    # else:
    #     if name[0] == "A":
    #         move -= 1

    return min(move_left, move_right)-1


print(solution("JEROEN"))
print(solution("JAN"))
