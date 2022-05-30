from collections import defaultdict
import sys
input = sys.stdin.readline
# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가
n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr = arr[:] + arr[:]  # 원형이므로 두 배로 늘려주기
left, right = 0, 0
result = 0
sushi = defaultdict(int)

# 처음에 k 만큼 먹기
for i in range(k):
    sushi[arr[right]] += 1
    right += 1

# 보너스 먹기
sushi[c] += 1

# k를 유지한 채로 움직이기
while right < len(arr):
    result = max(result, len(sushi))

    sushi[arr[left]] -= 1
    if sushi[arr[left]] == 0:  # 초밥이 없다면 제거
        del sushi[arr[left]]

    # 한 칸씩 이동
    left += 1
    sushi[arr[right]] += 1
    right += 1

print(result)
