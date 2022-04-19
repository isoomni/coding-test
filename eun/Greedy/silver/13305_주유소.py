# 13305 주유소
# 2202-04-13


n = int(input())
edge = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

oil_amount = 0
min_price = oil_price[0]  # 최소 기름값

for i in range(n-1):
    if oil_price[i] < min_price:
        min_price = oil_price[i]  # 최소 기름값 갱신

    oil_amount += min_price*edge[i]  # 최소 기름값의 가격으로 충전

print(oil_amount)


# n = int(input())
# edge = list(map(int, input().split()))
# oil_price = list(map(int, input().split()))

# oil_amount = 0
# cost = 0

# for i in range(n-1):
#     if i != 0:
#         oil_amount -= edge[i-1]
#     if oil_amount < edge[i]:
#         # 충전해야 할 리터 수 edge[i]-oil_amount
#         cost += oil_price[i]*(edge[i]-oil_amount)
#         oil_amount = edge[i]-oil_amount

# print(cost)

# n = int(input())
# edge = list(map(int, input().split()))
# oil_price = list(map(int, input().split()))

# oil_amount = 0
# cost = 0

# for i in range(n-1):

#     if oil_amount < edge[i]:
#         if min(oil_price[i:-1]) == oil_price[i]:
#             # 충전해야 할 리터 수 edge[i]-oil_amount
#             cost += oil_price[i]*(sum(edge[i:])-oil_amount)
#             oil_amount = sum(edge[i:])-oil_amount
#         else:
#             cost += oil_price[i]*(edge[i]-oil_amount)
#             oil_amount = edge[i]-oil_amount

#     oil_amount -= edge[i]

# print(cost)
