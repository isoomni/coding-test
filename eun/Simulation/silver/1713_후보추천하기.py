from collections import OrderedDict
n = int(input())
m = int(input())
arr = list(map(int, input().split()))

photo = OrderedDict()  # 순서가 보장되는 딕셔너리


def find_min():  # 최소 득표 학생찾기
    min_point = 1001
    student = 0
    for key, value in photo.items():
        if value < min_point:
            min_point, student = value, key
    return student


for i in arr:
    if i in photo:
        photo[i] += 1
    else:
        if len(photo) < n:
            photo[i] = 1
        else:
            student = find_min()  # 최소 득표 학생 찾은 후
            del photo[student]  # 제거하고
            photo[i] = 1  # 삽입

res = sorted(list(photo.keys()))
print(*res)
