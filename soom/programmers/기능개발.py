import math

progresses = list(map(int, (input().split())))
speeds = list(map(int, (input().split())))

def solution(progresses, speeds):
    # 100-93 // 7 올림
    # 100 - 30 // 30  math.ceil((100-progresses[i])//speeds[i])  -> 완료 일 수
    # 앞에 꺼 완료일수 < 뒤에 꺼 완료일수 -> 앞에 꺼 완료일수에 answer.append(1) continue
    # 앞에 꺼 완료일수 >= 뒤에 꺼 완료일수 -> 다시 앞에꺼 완료일수가 더 작은 인덱스까지 계속 cnt+=1 해서 +1 append continue
    answer = []
    day = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    
    front = 0
    for idx in range(len(day)):
        if day[front] < day[idx]:
            answer.append(idx-front)
            front = idx
        print('day',day[idx])
        print('front',front)
    print('front', front)
    answer.append(len(day)-front) # 마지막에 넣으면 됨

    return answer

# def solution(progresses, speeds):
#     answer = []
#     # 100-93 // 7 올림
#     # 100 - 30 // 30  math.ceil((100-progresses[i])//speeds[i])  -> 완료 일 수
#     # 앞에 꺼 완료일수 < 뒤에 꺼 완료일수 -> 앞에 꺼 완료일수에 answer.append(1) continue
#     # 앞에 꺼 완료일수 >= 뒤에 꺼 완료일수 -> 다시 앞에꺼 완료일수가 더 작은 인덱스까지 계속 cnt+=1 해서 +1 append continue
#     lp = len(progresses)
#     day = [0]*lp
#     for i in range(lp):
#         day[i] += math.ceil((100-progresses[i])//speeds[i])
#     print(day)
        
#     cnt = 1
#     front = 0
#     for j in range(front+1,len(day)):
#         if day[front] < day[j] and day[j] >= day[j+1]:
#             answer.append(cnt)
#             front = j
#         elif day[front] < day[j] and day[j] < day[j+1]:
#             front = j
#         elif day[front] >= day[j] and day[j] >= day[j+1]:
#             cnt += 1
#         elif day[front] >= day[j] and day[j] < day[j+1]:
#             cnt += 1
#             answer.append(cnt)

    
#     return answer

print(solution(progresses, speeds))