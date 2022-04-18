# def solution(phone_book):
#     answer = True

#     phone_book.sort(key=len)

#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False

#     return True

def solution(phone_book):
    answer = True

    phone_book.sort()  # 정렬을 한다. 그러면 접두어가 같은 순서대로 정렬이 될 것이다.

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:  # 접두어 비교
            return False

    return True


question = [["119", "97674223", "1195524421"], [
    "123", "456", "789"], ["12", "123", "1235", "567", "88"]]
for i in question:
    print(solution(i))
