# 집과 가장 가까운 치킨 집의 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 수익을 가장 많이 낼 수 있는 치킨집의 개수 M개
# 집에서 치킨 집까지의 거리
# 처음에는 각각의 치킨 집을 기준으로 치킨거리의 집이 많은 몇 개를 선택하려고 했음
# 3번 테케를 보고 치킨거리의 집의 개수가 모두 동일할 수 있음을 깨달음 -> itertools를 사용할 수 없음
# 치킨집의 경우의 수를 모두 조합하여 어떤 조합의 도시의 치킨거리가 가장 작은지 고려하여 돌려야 함.
# 완전탐색

import sys
from itertools import combinations
sys.stdin = open('soom/Samsung/test.txt', 'r')

n, m = map(int, input().split())  

# 지도 생성
data = [list(map(int,input().split())) for i in range(n)]
# print(data)
# [[1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1]]

# 치킨집과 집 각각의 좌표모음
chicken = [(i+1, j+1) for i, row in enumerate(data) for j, value in enumerate(row) if value == 2] 
home =  [(i+1, j+1) for i, row in enumerate(data) for j, value in enumerate(row) if value == 1] 
# print('chicken', chicken) 
# chicken [(1, 2), (1, 4), (2, 2), (2, 4), (3, 2), (3, 4), (4, 2), (4, 4), (5, 2), (5, 4)]
# print('home', home) 
# home [(1, 1), (1, 5), (2, 1), (2, 5), (3, 1), (3, 5), (4, 1), (4, 5), (5, 1), (5, 5)]

chicken_combi = []
# itertools - combinations -> 후에 직접 구현 코드로 변경해야 함.
for i in combinations(chicken, m):
    chicken_combi.append(i)
# print(chicken_combi)
# [((1, 2),), ((1, 4),), ((2, 2),), ((2, 4),), ((3, 2),), ((3, 4),), ((4, 2),), ((4, 4),), ((5, 2),), ((5, 4),)] 



# 치킨거리 계산식
# new = [home 좌표, chicken 좌표, 치킨거리]
# m = 2
result = []
chicken_dis = 0
for i in range(len(chicken_combi)):
    chicken_dis = 0
    for j in range(len(home)): # 하나의 home에 대한 모든 조합의치킨 거리 계산
        dis = n*n
        for k in range(m):
            if dis > (abs(home[j][0] - chicken_combi[i][k][0])) + (abs(home[j][1] - chicken_combi[i][k][1])):
                dis = (abs(home[j][0] - chicken_combi[i][k][0])) + (abs(home[j][1] - chicken_combi[i][k][1]))  # 치킨 거리 갱신
            # print('home',home[j],'chicken',chicken_combi[i][k],'dis', dis)

        chicken_dis+=dis # 첫 조합에 대해 모든 home의 치킨거리
        # print('chicken_dis', chicken_dis)
    result.append(chicken_dis)
print(min(result))

        
