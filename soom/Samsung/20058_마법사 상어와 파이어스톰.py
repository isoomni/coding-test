# 2^L * 2^L 크기의 부분 격자
# Q번 시행했다면 Q번 L단계를 정해서 바꿔줌
# 격자 안의 숫자를 시계 방향으로 90도 회전
# 칸 3개 이상과 인접해 있지 않으면(0이 아닌 칸 3개와 인접해있어야 함) 얼음 1 줄어듬
# N, Q 주어짐. 2^N * 2^N
# Q번 실행했을 때, 1. 남아 있는 얼음의 양 2. 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 출력
import sys
sys.stdin = open('20058.txt', 'r')
n, q = map(int, input().split())
len_data = 2 ** n
data = [list(map(int, input().split())) for _ in range(len_data)]
levels = list(map(int, input().split()))
# 격자를 만들어줘야?
# 회전하여 저장
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def rotate_and_melting(data, len_data, level):
    '''회전'''
    term = 2**level
    for x in range(0, len_data, term):
        for y in range(0, len_data, term):
            temp = [data[i][y:y + term] for i in range(x, x + term)]
            for i in range(term):  # 다음 격자까지의 거리 term이다.   열 인덱스
                for j in range(term): # 다음 격자까지의 거리 term이다.   행 인덱스
                    # 현재 격자의 N번째 열을  다음 격자의 N번째 행으로 바뀌도록 구성하면 된다.(90도 회전)
                    # N번째 열의 첫번째 원소는 N번째 행의 마지막 원소로, N번째 열의 마지막 원소는 N번째 원소의 첫번째 원소로 바뀌게 된다.
                    # (N번째 열 원소의 순서를 반전시키며 N번째 행으로 변환)
                    data[x+j][y+term-i-1] = temp[i][j]

    '''인접한 얼음 제거'''
    # 인접한 얼음을 비교하여, 3개 이상이 아닌 경우 얼음의 양 1 감소
    cnt = [[0] * len_data for i in range(len_data)]
    for i in range(len_data):
        for j in range(len_data):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < len_data and 0 <= ny < len_data and data[nx][ny]:
                    cnt[i][j] += 1

    # 인접한 얼음을 세는 것과 제거하는 것은 동시에 할 수 없다.
    # 그러므로 따로 제거해준다.
    for i in range(len_data):
        for j in range(len_data):
            if data[i][j] > 0 and cnt[i][j] < 3:
                data[i][j] -= 1

    # 남아 있는 얼음의 양

    return data

'''얼음 중 큰 덩어리가 차지하는 칸의 개수'''
# dfs 로 풀기
def dfs(x, y):
    result = 1
    data[x][y] = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < len_data and 0 <= ny < len_data and data[nx][ny]:
            result += dfs(nx, ny)  #재귀
    return result




def solve():
    for level in levels:
        dt = rotate_and_melting(data, len_data, level)
    print(sum(sum(i) for i in dt))

    ans = 0
    for x in range(n):
        for y in range(n):
            if data[x][y] > 0:
                ans = max(ans, dfs(x, y))
    print(ans, end='')

solve()