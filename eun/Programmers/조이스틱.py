# 23번만 통과 안됨
def solution(name):
    count = 0
    move = [0, 0, 0, 0]  # 오른쪽, 왼쪽, 오른쪽->왼쪽, 왼쪽->오른쪽
    nums = [0]*len(name)  # 0일 경우 A, 이외는 1 --> 연속된 A를 찾을 때 sum()==0으로 찾을 수 있음

    # 문자 변환
    for i in range(len(name)):
        if name[i] == "A":
            continue
        if ord(name[i])-ord("A") < 14:
            count += ord(name[i])-ord("A")
        else:
            count += 26-(ord(name[i])-ord("A"))
        nums[i] = 1
    nums[0] = 0  # 첫 번째는 이동하지 않아도 되므로 0으로 설정

    # 이동 계산
    # 오른쪽으로 이동
    for i in range(len(name)):
        if sum(nums[i+1:]) == 0:  # 남은 게 다 A라면
            break
        move[0] += 1

    # 왼쪽으로 이동
    move[1] += 1  # 첫 번째 칸에서 움직이는거 계산
    for i in range(len(name)-1, -1, -1):
        if sum(nums[:i]) == 0:  # 남은 게 다 A라면
            break
        move[1] += 1

    # 오른쪽 -> 왼쪽
    for i in range(len(name)):
        # 오른쪽 이동
        if name[i] == "A" and i+1 < len(name) and name[i+1] == "A":  # 연속된 A가 있다면
            index = i
            for j in range(i+1, len(name)+1):  # 연속된 A의 index 찾음
                if sum(nums[i:j]) != 0:
                    index = j-1
                    break

            if move[2] == 0:  # 첫 번째부터 A가 연속될 때
                move[2] = len(name)-index
            else:
                move[2] = (move[2]-1)*2+(len(name)-index)
            break
        else:
            move[2] += 1

    # 왼쪽 -> 오른쪽
    for i in range(len(name)-1, -1, -1):
        # 왼쪽 이동
        if name[i] == "A" and i-1 >= 0 and name[i-1] == "A":
            index = i
            for j in range(i-1, -1, -1):  # 연속된 A의 index 찾음
                if sum(nums[j:i]) != 0:
                    index = j
                    break
            if move[3] == 0:  # 맨 마지막부터 A가 연속될 때
                move[3] = index
            else:
                move[3] = (move[3]*2-1)+index+1
            break

        else:
            move[3] += 1

    return count+min(move)


# print(solution("JEROEN"))  # 56
# print(solution("JAN"))  # 23
# print(solution("LABLPAJM"))  # answer:61
# print(solution("BMOABA"))  # answer:30
# print(solution("LAABAA"))  # answer:15
# print(solution("AAAAAAAAJAAAA"))  # answer:14
# print(solution("SAAAAAARRM"))  # answer:41
# print(solution("RABAMATAWADLAFAVAAE"))  # answer:78
# print(solution("XAAAAAABA"))  # answer:6
# print(solution("AYOZAAVADAY"))  # answer:35
# print(solution("AAFEASAAVA"))  # answer:30
# print(solution("UAGAAASAAFAFXZA"))  # answer:47
# print(solution("AAAAZAATAEA"))  # answer:19
# print(solution("AACALATLAHABAA"))  # answer:50
# print(solution("FAWJAAAFV"))  # answer:35
# print(solution("AACAVAAPSAAOAA"))  # answer:49
# print(solution("AKAAWAKX"))  # answer:33
# print(solution("LOAAAHAJAAFAEBAWO"))  # answer:79
# print(solution("AWAWVAQVAAA"))  # answer:35
# print(solution("RCETAAAAVUEAETZAAAK"))  # answer:75
# print(solution("GTAASKKAE"))  # answer:52
# print(solution("AAAABAAAAAAKSAIQ"))  # answer:49
# print(solution("ADASAAAUAAAPAA"))  # answer:39
# print(solution("AAAAADBAAELSPUAAAOA"))  # answer:70
# print(solution("VJAAIAFNAAAAA"))  # answer:47
# print(solution("AARUAUAAHTBJAAYS"))  # answer:69
# print(solution("IASAGITUPHE"))  # answer:74
# print(solution("AAALAAAAAA"))  # answer:14
# print(solution("AAAEASAHQAYTAAAJ"))  # answer:60
# print(solution("BAALEAAAPMAAAHSRAV"))  # answer:83
# print(solution("ASWAAATDAJAXA"))  # answer:45
# print(solution("DYAOAAAARQANAWA"))  # answer:66
# print(solution("AAIAPB"))  # answer:24
# print(solution("BBBBAAAABA"))  # 12
# print(solution("ABABAAAAAAABA")) #10
# print(solution("BBABAAAABBBAAAABABB"))  # 26
# print(solution("BBAAAAAABBBAAAAAABB"))  # 20
# print(solution("BBBAAAAAAAB"))  # 8
# print(solution("ABAAAAAAAAABB"))  # 7
# print(solution("BBAABB"))  # 8
# print(solution("BBBAAAAABAAAAAAAAAAA"))  # 12
# print(solution("BAAAAAAAAAABAAAAAABB"))  # 13
# print(solution("AAABBAB"))  # 7
print(solution("ABABAAAAABA"))
