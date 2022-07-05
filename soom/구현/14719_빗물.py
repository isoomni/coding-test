'''
특정 위치에 물이 고이기 위해선 자신보다 더 높은 블록으로 왼쪽과 오른쪽이 둘러싸여 있어야한다.
그리고 이 조건을 만족할 때, 물이 고이는 양은 왼쪽과 오른쪽 블록 중 더 낮은 블록과 현 위치의 값이다.
만약 높이가 1인 구역을 왼쪽 오른쪽으로 각각 3, 4 높이의 블록이 감싸고 있다면 해당 구역은 더 낮은 블록인 3에서 현 위치의 높이인 1을 뺀 2 만큼의 물이 고인다.
첫 번째 칸과 마지막칸은 물이 고일 수 없으므로 range를 1부터 w - 1까지 잡아주고 각 위치마다 알맞는 양의 물을 채워넣으면 답을 구할 수 있다.
'''

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
data = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(data[:i])
    right_max = max(data[i+1:])

    compare = min(left_max, right_max)

    if data[i] < compare:
        ans += compare - data[i]

print(ans)
