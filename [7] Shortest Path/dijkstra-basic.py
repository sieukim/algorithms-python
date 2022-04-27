# ****** 표준 입력 ****** #
import sys

# sys.stdin.readline을 이용하여 한줄씩 표준 입력을 받는 함수
input = sys.stdin.readline

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 대한 연결 노드 정보를 나타내는 리스트
graph = [[] for _ in range(n + 1)]

# 그래프 초기화
for _ in range(m):
    # 노드 node1에서 노드 node2로 가는데 필요한 거리 d
    node1, node2, d = map(int, input().split())
    graph[node1].append((node2, d))


# ****** 변수 선언 ****** #

# 무한을 의미(10억)
inf = int(1e9)

# 방문 기록 리스트
visited = [False] * (n + 1)

# 최단 거리 테이블, 무한으로 초기화
distance = [inf] * (n + 1)


# ****** 함수 선언 ****** #

# 방문하지 않은 노드 중, 가장 짧은 최단 거리를 갖는 노드의 번호를 반환하는 함수
def get_min_distance_node():
    # 가장 짧은 최단 거리
    min_distance = inf
    # 가장 짧은 최단 거리를 갖는 노드의 번호
    min_distance_node = 0

    for i in range(1, n + 1):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            min_distance_node = i
    
    return min_distance_node


# ****** 간단한 다익스트라 알고리즘 수행 ****** #
# *** 시간 복잡도: O(V ^ 2)
# *** 권장 노드 개수: 5000개 이하

# 시작 노드 방문 기록 갱신
visited[start] = True
# 시작 노드 최단 거리 갱신
distance[start] = 0 
# 시작 노드랑 인접한 노드의 최단 거리 갱신
for [node, d] in graph[start]:
    distance[node] = d

# 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
for i in range(n - 1):
    # 현재 가장 짧은 최단 거리를 갖는 노드의 번호
    min_distance_node = get_min_distance_node()
    # 해당 노드에 대한 방문 기록 갱신
    visited[min_distance_node] = True
    # 해당 노드와 인접한 노드의 최단 거리 갱신
    for [node, d] in graph[min_distance_node]:
        # 해당 노드를 거쳐 다른 노드로 이동하는 거리와 해당 노드의 기존 최단 거리를 비교하여 최소값으로 갱신
        distance[node] = min([distance[min_distance_node] + d, distance[node]])


# ****** 출력 ****** #

# 시작 노드에서 출발하여
# 다른 모든 노드에 도착하는데
# 걸리는 최단 거리를
# 모두 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, INF 출력
    if distance[i] == inf:
        print('INF')
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])




# 예제 1
#
# 입력
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# 
# 출력
# 0
# 2
# 3
# 1
# 2
# 4