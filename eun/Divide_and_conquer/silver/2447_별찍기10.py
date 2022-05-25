n = int(input())
star = ["***", "* *", "***"]
cnt = 0


def getStars(star):
    mat = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            mat.append(star[i % len(star)] + " " *
                       len(star) + star[i % len(star)])
        else:
            mat.append(star[i % len(star)] * 3)
    return mat


for i in range(int(n**(1/3))-1):
    star = getStars(star)

for i in star:
    print(i)
