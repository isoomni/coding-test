# 짝수 사이에 있는 홀수를 삭제
'''
포인터 두 개 (lp, rp)를 선언한 후 rp를 홀수의 개수가 K가 넘을 때 까지 늘려줍니다.
(rp의 위치를 옮기다가 리스트의 길이를 넘어가는 것도 처리)
K개를 넘었다면 바로 한 칸 전으로 옮겨주어 K개를 넘기 바로 직전에 rp를 위치합니다.

그 후 lp과 rp사이에 있는 짝수의 개수를 계산합니다. # (rp의 위치 - lp의 위치 + 1 - 홀수의 개수)
그러고 나서 lp의 값을 오른쪽으로 옮겨줍니다. (이 때 기존 lp이 가리키는 값이 홀수라면 홀수 -1)
lp의 이동으로 인해 홀수의 개수가 줄게 되면, 다시 rp가 움직이기 시작하고, 이 과정을 반복하면 됩니다.
'''

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = list(map(int, input().split()))

lp, rp = 0, 0
answer = 0
odd_cnt = 0
temp_cnt = 0

