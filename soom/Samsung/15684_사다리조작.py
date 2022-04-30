# n, m, h
# 세로, 가로, 가로 가능
# 가로선 정보 (a,b)
# 조작하는 가로선은 얼마든지 더 추가가능
# 결과적으로 +-0이 되어야함.
# 출력: 몇 개의 선을 더 추가해야 하는가?

import sys
from itertools import combinations
sys.stdin = open('soom/Samsung/15684.txt', 'r')

n, m, h = map(int, input().split())

data = [list(map(int, input().split())) for i in range(m)]

