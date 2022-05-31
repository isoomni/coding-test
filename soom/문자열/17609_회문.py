"""
투 포인터를 이용한 회문 검사
- 회문: 0 (앞뒤 동일)
- 유사회문: 1 (한 문자 삭제 시 앞뒤 동일)
- 둘다 해당 안됨: 2
:return:
"""
import sys

string = sys.stdin.readline
n = int(input())


def is_palindrome(data):
    left = 0
    right = len(data) - 1
    if data == data[::-1]:
        return 0
    else:
        while left < right:
            # 1. left right 문자가 동일한 경우:  left + 1, right + 1
            if data[left] == data[right]:
                left += 1
                right -= 1
            else:
                # 2. left right 다른 경우: 한 문자열 제거 후 회문 확인
                # 2-1. 오른쪽 문자열 제거한 경우 제거 후 회문이되는지 확인
                if left < right - 1:
                    temp = data[:right] + data[right + 1:]
                    if temp[:] == temp[::-1]:
                        return 1
                # 2-2. 왼쪽 문자열 제거한 경우 제거 후 회문이되는지 확인
                if left + 1 < right:
                    temp = data[:left] + data[left + 1:]
                    if temp[:] == temp[::-1]:
                        return 1
                # # 2-3. 회문이 안된 경우, 2리턴
                return 2


for _ in range(n):
    data = input()
    print(is_palindrome(str(data)))
