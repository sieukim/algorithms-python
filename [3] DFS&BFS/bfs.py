from collections import deque

# bfs 함수
def bfs(graph, v, visited):
    # 큐 
    queue = deque([v])
    # 현재 노드 방문 처리
    visited[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 최하위 노드 제거
        v = queue.popleft()
        # 최하위 노드 출력
        print(v, end=' ')
        # 최하위 노드의 인접 노드 모두 큐에 추가
        for node in graph[v]:
            # 방문하지 않는 노드인 경우
            if not visited[node]:
                queue.append(node)
                visited[node] = True



# 인접 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 여부
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)