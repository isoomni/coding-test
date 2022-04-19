# 정확성 100, 효율성 0

import pandas as pd

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

data = []
q = []
for i in range(len(info)):
    data.append(info[i].split())

df = pd.DataFrame(data, columns=['lang','category','exp','food','score'])
df = df.astype({'score':int})
print(df)

for i in range(len(query)):
    q.append(query[i].replace('and ','').split())

for j in range(len(q)):
    data = df
    for k in range(5):
        print('몇번째 조건인지?(lang category exp food score)',k)
        if q[j][k] == '-' :
            continue
        elif k == 0:
            data = data[(data.lang == q[j][k])]
        elif k ==1:
            data = data[(data.category == q[j][k])]
        elif k ==2:
            data = data[(data.exp == q[j][k])]
        elif k ==3:
            data = data[(data.food == q[j][k])]
        elif k ==4:
            data = data[(data.score >= int(q[j][k]))]

    print('df길이',len(data))

    # print(len(df[(df.lang == q[j][0]) & (df.category == q[j][1]) & (df.exp == q[j][2]) & (df.food == q[j][3]) & (df.score > q[j][4])]))




print(q)