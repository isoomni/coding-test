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
for j in v:
    answer *= (v[j]+1)
answer -= 1

print(answer)