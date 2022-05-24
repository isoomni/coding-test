n = int(input())
star = ["  *  ", " * * ", "*****"]


def solution(star, space):
    temp = []
    for i in range(len(star)*2):
        if i//len(star) == 0:  # 원본
            temp.append(" "*space + star[i % len(star)] + " "*space)
        else:  # 늘리기
            temp.append(star[i % len(star)]+" "+star[i % len(star)])
    return temp


cnt = 0
n = n/3
while n > 1:
    n = n/2
    cnt += 1

space = 3  # 공백

for _ in range(1, cnt+1):
    star = solution(star, space)
    space *= 2

for i in star:
    print(i)
