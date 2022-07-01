from collections import deque

# 노드와 간선의 개수
v, e = map(int, input().split())
# 진입차수 리스트 초기화
indegree = [0] * (v + 1)
# 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 수행 결과
result = []
# 큐
q = deque()

# 진입차수가 0인 노드를 큐에 삽입
for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    # 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
        indegree[i] -= 1
        # 진입차수가 0이 된 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i, end=' ')


# 예제 1
#
# 입력
# 7 8
# 1 2 
# 1 5 
# 2 3 
# 2 6 
# 3 4 
# 4 7 
# 5 6 
# 6 7 
#
# 출력
# 1 2 5 3 6 4 7 