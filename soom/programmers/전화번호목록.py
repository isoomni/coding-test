# # 효율성 0 / 정확성 100
# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=lambda x: len(x))
#     ln = len(phone_book)
    
#     for i in range(ln):
#         for j in range(i+1,ln):
#             if i == j:
#                 continue
#             elif phone_book[i] == phone_book[j][0:len(phone_book[i])]:
#                 answer = False
#                 break
        
#     return answer

# 효율성 100 / 정확성 100
def solution(phone_book):
    answer = True
    phone_book.sort()
    ln = len(phone_book)
    
    for i in range(ln-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                answer = False
                break
        
    return answer
