# 무한
INF = int(1e9)

# 전체 회사 개수와 경로 개수
n, m = map(int, input().split())

# graph[i][j]: graph[i][k]에서 graph[k][j]로 가는 최소 비용
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# graph 초기화
for i in range(1, n + 1):
    # 자기 자신까지의 최단 거리 = 0
    graph[i][i] = 0

# 연결된 두 회사 번호 
for _ in range(m):
    # node1와 node2 사이의 거리 1
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

# x: 도착 회사, k: 경유 회사
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1번 회사에서 출발하여 k번 회사를 거쳐 x번 회사에 도착할 때, 최소 비용
answer = graph[1][k] + graph[k][x]

# 경로가 없는 경우
if answer >= INF:
    # -1 출력
    print(-1)
# 경로가 존재하는 경우
else:
    # 최소 비용 출력
    print(answer)


# 예제 1
#
# 입력
# 5 7
# 1 2
# 1 3 
# 1 4 
# 2 4 
# 3 4
# 3 5
# 4 5
# 4 5
#
# 출력
# 3

# 예제 2
#
# 입력
# 4 2 
# 1 3
# 2 4 
# 3 4 
#
# 출력
# -1