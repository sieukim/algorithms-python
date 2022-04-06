# dfs 함수
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    # 현재 노드 출력
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for node in graph[v]:
        # 방문하지 않은 노드인 경우
        if not visited[node]:
            dfs(graph, node, visited)

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
dfs(graph, 1, visited)