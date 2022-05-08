# def solution(n, k, cmd):
#     num = [True] * n
#     index = k
#     delete = []
#     for i in cmd:
#         if i[0] == "U":
#             count = int(i[2])
#             while count > 0:
#                 if num[index-1]:
#                     count -= 1
#                 index -= 1
#         elif i[0] == "D":
#             count = int(i[2])
#             while count > 0:
#                 if num[index+1]:
#                     count -= 1
#                 index += 1
#         elif i[0] == "C":
#             num[index] = False
#             delete.append(index)
#             if any(num[index+1:]):
#                 while True:
#                     index += 1
#                     if num[index] == True:
#                         break
#             else:
#                 while True:
#                     index -= 1
#                     if num[index] == True:
#                         break
#         elif i[0] == "Z":
#             num[delete[-1]] = True
#             delete.pop()

#     result = ""
#     for i in num:
#         if i:
#             result += "O"
#         else:
#             result += "X"
#     return result

# def solution(n, k, cmd):
#     num = [i for i in range(n)]
#     index = k
#     delete = []
#     for i in cmd:
#         if i[0] == "U":
#             index -= int(i[2])
#         elif i[0] == "D":
#             index += int(i[2])
#         elif i[0] == "C":
#             delete.append(num.pop(index))
#             if index == len(num):
#                 index -= 1
#         elif i[0] == "Z":
#             p = delete.pop()
#             if p < num[index]:
#                 index += 1
#             num.append(p)
#             num.sort()

#     x = 0
#     result = ""
#     for i in range(n):
#         if num[x] == i:
#             result += "O"
#             x += 1
#         else:
#             result += "X"

#     return result

def solution(n, k, cmd):
    index = k
    table = {i: [i-1, i+1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    answer = ["O"]*n

    delete = []

    for i in cmd:
        if i == "C":  # 삭제
            answer[index] = "X"
            prev, next = table[index]
            delete.append([prev, index, next])

            if next == None:  # 마지막 행을 삭제했을 때
                index = table[index][0]
            else:
                index = table[index][1]

            if prev == None:  # 첫 번째 행을 삭제했을 때
                table[next][0] = None
            elif next == None:  # 마지막 행을 삭제했을 때
                table[prev][1] = None
            else:  # 가운데 있는 행을 삭제했을 때
                table[prev][1] = next
                table[next][0] = prev

        elif i == "Z":  # 복구
            prev, now, next = delete.pop()
            answer[now] = "O"
            if prev == None:  # 삭제한 행이 첫 번째 행이었을 때
                table[next][0] = now
            elif next == None:  # 삭제한 행이 마지막 행이었을 때
                table[prev][1] = now
            else:  # 삭제한 행이 가운데에 있던 행이었을 때
                table[next][0] = now
                table[prev][1] = now
        else:
            c1, c2 = i.split()
            if c1 == "D":
                for _ in range(int(c2)):
                    index = table[index][1]
            else:
                for _ in range(int(c2)):
                    index = table[index][0]

    return "".join(answer)


# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
