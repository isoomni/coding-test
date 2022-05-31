import sys
from collections import defaultdict
input = sys.stdin.readline

def string_game(W, K):
    if K == 1:  # k가 1이면 문자열은 무조건 1
        return [1, 1]
    alphabet = defaultdict(int)  # 각 알파벳의 숫자를 담을 딕셔너리
    interval = []

    for i in W:
        alphabet[i] += 1
    for key, value in alphabet.items():
        if value >= K:  # 알파벳 중 숫자가 k개 이상인 것만 보이위해
            index_list = list(filter(lambda x: W[x] == key, range(len(W))))

            for j in range(len(index_list)-K+1): # 알파벳 인덱스 사이 길이
                interval.append(index_list[j+K-1] - index_list[j])

    if not interval:  # 검색 실패
        return [-1]
    return [min(interval)+1, max(interval)+1]

T = int(input())
for _ in range(T):
    W = str(input())
    K = int(input())
    print(*string_game(W, K))