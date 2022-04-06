'''
아이디어
1. 정점과 간선이 있다.
2. 정점에는 번호가 있다.
3. 간선은 어떤 정점을 잇는 간선인지에 대한 정보와, 해당 간선의 가중치에 대한 정보가 주어진다.
4. 같은 점에서 같은 점으로 가는 간선은 없다.
5. 가중치는 10 이하이다.
6. 서로 다른 두 정점 사이에 여러 개의 간선이 있을 수 있따.

'''
V, E = map(int, input().split())
start = int(input())
data = []
for e in range(E):
    data.append(list(map(int, (input().split()))))
print(data)

