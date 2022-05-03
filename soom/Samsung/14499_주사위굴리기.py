N, M, r, c, K = map(int, input().split())
mp = []
for i in range(N):
    mp.append(list(map(int, input().split())))

command = list(map(int, input().split()))
dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for k in range(K):
    
    if command[k] == 1:
        c += 1
        if c >= M or c < 0:
            c -= 1
            continue
        else:
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif command[k] == 2:
        c -= 1
        if c >= M or c < 0:
            c += 1
            continue
        else:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif command[k] == 3:
        r -= 1
        if r >= N or r < 0:
            r += 1
            continue
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif command[k] == 4:
        r += 1
        if r >= N or r < 0:
            r -=1
            continue
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

    if mp[r][c] == 0:
        mp[r][c] = dice[6]
    elif mp[r][c] != 0:
        dice[6] = mp[r][c] # 주사위 밑에 지도 시작부분 r,c 값을 담는다.
        mp[r][c] = 0  # 지도 시작 부분에는 0을 내린다.
    
    print(dice[1])

