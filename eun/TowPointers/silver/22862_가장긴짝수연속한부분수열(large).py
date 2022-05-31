n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
result = 0
delete = 0  # 삭제한 개수
while right < n:
    if arr[right] % 2 == 0:  # 짝수라면 right 증가
        right += 1
    else:  # 홀수일 때
        if delete < k:  # 아직 삭제할 수 있다면
            delete += 1
            right += 1

        else:  # 삭제할 수 없다면
            result = max(result, right-left-delete)
            while True:  # left에서 홀수가 나올 때 까지 while문 돌리기
                if arr[left] % 2 == 1:
                    delete -= 1
                    left += 1
                    break
                left += 1
print(max(result, right-left-delete))  # while 문을 다 돌고 난 다음의 결과와 result 비교
