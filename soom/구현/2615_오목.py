# 브루트 포스
# 방향을 (→ ↓ ↘ ↗)로 설정
# 모든 좌표에서 방향 갯수만큼 for문을 4번 돌려 → ↓ ↘ ↗ 방향으로 쭉쭉 5칸씩을 체크
# 육목은 이긴 것이 아니다.
import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        # 칸이 0이 아니면 거기서부터 탐색한다.
        if data[x][y] != 0:
            focus = data[x][y]
            for i in range(4): # 방향 갯수만큼 for문을 돌려서 5칸씩 체크한다.
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and data[nx][ny] == focus: # 같은 돌이 연속함
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        # 첫번째 바둑돌보다 한 칸 이전의 바둑돌 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and data[x - dx[i]][y - dy[i]] == focus:
                            break
                        # 마지막 바둑돌보다 한 칸 이후의 바둑돌 체크
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and data[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        # 육목이 아니면 성공한거니까 종료
                        print(focus)
                        print(x + 1, y + 1)
                        # 승리판정시 더이상의 좌표를 탐색하지 않기 위해 이 모든 반복문을 빠져나올 방법이 필요했다.
                        # 프로그램이 정상적으로 종료가 됐다는 것을 표시할 때는 sys.exit 인자값을 0으로 주고
                        # 비정상적으로 종료가 됐다는 것을 표시할 때는 sys.exit 인자값을 1을 주면 된다.
                        # sys.exit(0)을 실행하면 굳이 불린값으로 종료체크를 하지 않아도 바로 프로그램을 정상 종료시킬 수 있다
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)


