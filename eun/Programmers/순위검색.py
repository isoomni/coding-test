# def solution(info, query):
#     info_list = [i.split() for i in info]

#     result = []

#     for i in query:
#         q = i.split()
#         count = 0
#         for j in range(len(info_list)):
#             if q[0] != "-":
#                 if info_list[j][0] != q[0]:
#                     continue
#             if q[2] != "-":
#                 if info_list[j][1] != q[2]:
#                     continue

#             if q[4] != "-":
#                 if info_list[j][2] != q[4]:
#                     continue

#             if q[6] != "-":
#                 if info_list[j][3] != q[6]:
#                     continue

#             if int(info_list[j][4]) < int(q[7]):
#                 continue

#             count += 1
#         result.append(count)
#     return result


def solution(info, query):

    hashmap = {}

    info_list = [i.split() for i in info]

    for i in query:
        q = i.split()
        count = 0
        for j in range(len(info_list)):
            h = []
            if q[0] == "-":
                h.append("java")
                h.append("cpp")
                h.append("python")
            else:
                h.append(q[0])

            if q[2] == "-":
                for k in range(len(h)):
                    h[k] += "backend"
                    h.append(h[k]+"frontend")
            else:
                for k in range(len(h)):
                    h[k] += q[2]

            if q[4] == "-":
                for k in range(len(h)):
                    h[k] += "junior"
                    h.append(h[k]+"senior")
            else:
                for k in range(len(h)):
                    h[k] += q[4]

            if q[6] == "-":
                for k in range(len(h)):
                    h[k] += "chicken"
                    h.append(h[k]+"pizza")
            else:
                for k in range(len(h)):
                    h[k] += q[6]

            for k in h:
                hashmap[k] = int(q[7])

        print(hashmap)
        result.append(count)
    return result


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
