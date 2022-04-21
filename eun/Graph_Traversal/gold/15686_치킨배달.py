# 15686 치킨 배달
# 2022-04-20

from itertools import combinations

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

chickens = []
homes = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            homes.append([i, j])
        elif grid[i][j] == 2:
            chickens.append([i, j])

chicken_load = n**3
chicken_list = combinations(chickens, m)

for chicken in chicken_list:
    # chicken -> 치킨집 중 m개 고름
    min_dist = [n*2]*len(homes)
    for i in range(len(homes)):  # 집을 순회하면서
        for a, b in chicken:  # m개의 치킨집과의 거리를 계산.
            if abs(homes[i][0]-a)+abs(homes[i][1]-b) < min_dist[i]:
                min_dist[i] = abs(homes[i][0]-a)+abs(homes[i][1]-b)

    if chicken_load > sum(min_dist):
        chicken_load = sum(min_dist)

print(chicken_load)
