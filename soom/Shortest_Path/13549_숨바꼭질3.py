'''
점은 10만개이다.

2배를 가면 0초
+1 -1 을 가면 1초 더해진다.
queue에 넣는다?
visited에 지난간 점을 넣는다.
탐색할 점을 넣는다.

---
present = 5를 2배 한 값.
present == k이면 출력
아니면 

present = +1 한다.
present == k이면 출력
아니면 원래값으로 초기화

present = -1한다.
present == k이면 출력
아니면 원래값으로 초기화

---
bfs로 
2배를 먼저
queue에

'''

from collections import deque 
n, k = map(int, input().split()) # n: 수빈이가 있는 위치, k: 동생이 있는 위치 
q = deque() 
q.append(n) 
MAX = 100001
visited = [-1 for _ in range(MAX)] 
visited[n] = 0 


while q: 
    s = q.popleft() 

    if s == k: 
        print(visited[s]) 
        break 

    if 0 < s*2 < MAX and visited[s*2] == -1: 
        visited[s*2] = visited[s] 
        q.appendleft(s*2)     # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함 
        
    if 0 <= s-1 < MAX and visited[s-1] == -1: 
        visited[s-1] = visited[s] + 1 
        q.append(s-1) 
        
    
    if 0 <= s+1 < MAX and visited[s+1] == -1: 
        visited[s+1] = visited[s] + 1 
        q.append(s+1)

