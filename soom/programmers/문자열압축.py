s = input()
answer = len(s)

l = len(s)

data = []
result = ''
cnt = 0

for j in range(1, l): # 약수로만 자를 수 있다. j = 단위

        for i in range(0, l, j):
            data.append(s[i:i+j])
        
        for a in range(0, len(data)):
            # 이전 문자열과 현재 문자열이 같고, 현재 문자열이 다음 문자열과 같으면 하나 더 가야하니까 cnt+=1하고 다음으로
            # 이전 문자열과 현재 문자열이 같은데 다음 문자열이랑은 달라진다면 cnt와 해당 문자열을 출력, cnt =0으로 초기화
            # 이전 문자열과 현재 문자열이 다른데, 현재 문자열과 다음 문자열이 같으면 다음에서 처리해주도록 continue
            # 이전 문자열과 현재 문자열이 다른데, 현재 문자열과 다음 문자열도 다르면 그냥 현재 문자열을 출력 cnt = 0
            if a == 0: # a가 첫 인덱스라면,
                if (data[a]) == (data[a+1]): 
                    continue
                elif (data[a]) != (data[a+1]):
                    result += str(data[a])
              
            elif a == len(data)-1: # a가 마지막 인덱스이면,
                if (data[a-1]) == (data[a]): 
                    result += str(data.count(data[a])) + str(data[a])
                    cnt = 0  
                elif (data[a-1]) != (data[a]):
                    result += str(data[a])
                    cnt = 0
            else:
                if (data[a-1]) == (data[a]) and (data[a]) == (data[a+1]): #
                    cnt += 1  
                elif (data[a-1]) == (data[a]) and (data[a]) != (data[a+1]): 
                    result += str(data.count(data[a])) + str(data[a])
                    cnt = 0  
                elif (data[a-1]) != (data[a]) and (data[a]) == (data[a+1]):
                    continue
                elif (data[a-1]) != (data[a]) and (data[a]) != (data[a+1]):
                    result += str(data[a])
                    cnt = 0

        data = [] # 초기화
                
        if len(result) < answer:    
            answer = len(result)
        
        result = ''
    

    
print(answer)