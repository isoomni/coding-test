def solution(name):
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # 'A' == 65
    move = 0
    now = 0

    for i in range(len(name)):
        if name == "A":
            continue

        if ord(name[i])-ord("A") < 14:
            move += ord(name[i])-ord("A")
        else:
            move += 26-(ord(name[i])-ord("A"))

        move += 1

    if len(name) > 1:
        if name[0] == "A" or name[1] == "A":
            move -= 1
    else:
        if name[0] == "A":
            move -= 1

    return move
