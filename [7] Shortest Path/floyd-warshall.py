# 무한을 나타내는 상수
INF = int(1e9)

# ****** 표준 입력 ****** #

# 노드 개수, 간선 개수 입력 받기
n = int(input())
m = int(input())

# graph[i][j]: graph[i][k]에서 graph[k][j]로 가는 최소 비용
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 그래프 초기화 - 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 그래프 초기화
for _ in range(m):
    # 노드 node1에서 노드 node2로 가는데 필요한 거리 d
    node1, node2, d = map(int, input().split())
    graph[node1][node2] = d

# ****** 플로이드 워셜 알고리즘 수행 ****** #
# *** 시간 복잡도: O(n ** 3)

# D(ab) = min(D(ab), D(ak) + D(kb))
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# ****** 출력 ****** #

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print("")


# 예제 1
#
# 입력
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

# 출력
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0