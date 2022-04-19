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


def find_people(array, target):
    left, right = 0, len(array)

    while left < right:
        mid = (left+right)//2

        if array[mid] < target:
            left = mid+1
        else:
            right = mid

    return len(array)-right


def solution(infos, queries):
    answer = []

    info_dict = {}

    # 나올 수 있는 모든 경우의 수
    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    info_dict[lang + job + career + food] = []

    # 지원자의 경우의 수 (1인, 16가지)
    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        # 해당하는 경우의 수에 점수 append
                        info_dict[lang + job + career +
                                  food].append(int(info[4]))

    # info_dict의 key를 sort -> Lower bound 사용 가능!
    for key in info_dict.keys():
        info_dict[key].sort()

    # 쿼리문 돌면서 해당하는 지원자의 수 파악
    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()

        query_score = int(query[1])  # 점수
        query = query[0]  # 쿼리문

        info_score = info_dict[query]
        people_num = find_people(info_score, query_score)

        answer.append(people_num)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
