n, k = map(int, input().split())
number = list(map(int, input().split()))

need = {}

for i in set(number):
    # 사용 가능한 수 만큼 저장
    # 예) need = {1:2, 2:2, 3:3, 4:2}
    need[i] = k

left, right = 0, 0
result = 0

while right < n:
    num = number[right]  # 현재 탐색하고 있는 숫자

    if need[num] > 0:  # 아직 사용할 수 있다면
        need[num] -= 1  # need에서 감소시키고
        right += 1  # right 포인터 증가
    else:  # 만약에 다 사용했다면
        if result < right-left:  # 결과 갱신
            result = right-left

        while need[number[right]] < 1:  # right에 있던 숫자가 범위에서 빠질 때 까지
            need[number[left]] += 1  # 왼쪽 포인터 증가
            left += 1

if result < right-left:
    result = right-left

print(result)
