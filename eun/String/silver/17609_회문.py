def is_palindrome(s, cnt):
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            break
        left += 1
        right -= 1
    else:
        return cnt

    if cnt > 1:  # cnt가 1이상이면 return 2
        return 2

    temp1 = is_palindrome(s[left:right], cnt+1)  # 오른쪽 하나 줄여서
    temp2 = is_palindrome(s[left+1:right+1], cnt+1)  # 왼쪽 하나 늘려서

    if temp1 == 1 or temp2 == 1:  # temp1,2 중 하나가 1이라면
        return 1
    else:
        return 2


n = int(input())
for _ in range(n):
    cnt = is_palindrome(input(), 0)
    print(cnt)
