prices = list(map(int,input().split()))

def solution(prices):  
    # 만약 p보다 작은 값이 끝까지 없으면 len(prices)-(p의 인덱스)-1
    # 만약 p보다 작은 값이 나오면, (작은 값의 인덱스) - (p의 인덱스)

    lnp = len(prices)
    answer = [0]*lnp    
    for i in range(lnp):
        for j in range(i+1,lnp):
            if prices[i] > prices[j]: # p값이 비교값보다 떨어졌다.
                answer[i] += 1
                break 
            elif prices[i] <= prices[j]: # 안떨어졌다.
                answer[i] += 1
                continue
    
    return answer

print(solution(prices))