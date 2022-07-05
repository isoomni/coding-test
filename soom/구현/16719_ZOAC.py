import sys
input = sys.stdin.readline

data = list(input().strip())

start = 0
opening = ['']*len(data)
temp = 'a'
flag = True
while True:
    if not 'a' in data[start:]:
        start = data.index(min(data[start:]))
        opening[start] = data[start]
        print(''.join(opening))
        data[start] = temp
        if start >= len(data)-1:  # 홀수
            flag = False


    if flag == True:
        start += 1
    else:
        start -= 1


