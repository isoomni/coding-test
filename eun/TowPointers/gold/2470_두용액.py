# 2470 두 용액
# 220512

n = int(input())
array = list(map(int, input().split()))
array.sort()

left, right, start, end = 0, n-1, 0, n-1

while left < right:
    if abs(array[start]+array[end]) > abs(array[left]+array[right]):  # 정답 갱신
        start, end = left, right

    # 다음으로 움직일 포인터 정하기
    # 이동했을 때 0에 더 가까운 쪽으로 이동
    if abs(array[left+1]+array[right]) > abs(array[left]+array[right-1]):
        right -= 1
    else:
        left += 1

print(array[start], array[end])
