# 40분 소요
# 서로 다른 카테고리 끼리만 조합 가능
# 혼자서 조합가능
# 11시30분 시작
# headgear가 이전에 나온 적 없이 처음 나온거라면 v에 넣고 개수를 1개 더함
# 이전에 나온 적 있다면 headgear에 1을 더함
# 그 ()이걸로 하는게 좋을듯

clothes= [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 1
cl = len(clothes)
cnt = cl # 혼자서 조합
v = {}
for i in range(cl):
    if clothes[i][1] not in v:
        v[clothes[i][1]] = 1
    elif clothes[i][1] in v:
        v[clothes[i][1]] += 1
    print(v)

# 스파이가 옷을 입는 경우 의 수 = (A 옷 보유 수 + 1) (B 옷 보유 수 + 1) (C 옷 보유 수 + 1) - 1(아무것도 입지 않는 경우)
for j in v:
    answer *= (v[j]+1)
answer -= 1

print(answer)