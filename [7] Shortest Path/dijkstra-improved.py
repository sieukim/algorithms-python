import sys
import heapq

# ****** 표준 입력 ****** #

# sys.stdin.readline을 이용하여 한줄씩 표준 입력을 받는 함수
input = sys.stdin.readline

# 노드 개수, 간선 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())

# 각 노드에 대한 연결 노드 정보를 나타내는 리스트
graph = [[] for _ in range(n + 1)]

# 그래프 초기화
for _ in range(m):
    # 노드 node1에서 노드 node2로 가는데 필요한 거리 d
    node1, node2, d = map(int, input().split())
    graph[node1].append((node2, d)) 

# ****** 변수 선언 ****** #

# 무한을 나타내는 상수
INF = int(1e9)

# 최단 거리 테이블
distance = [INF] * (n + 1)

# ****** 개선된 다익스트라 알고리즘 수행 ****** #
# *** 시간 복잡도: O(ElogV)

# 우선순위 큐
# (시작 노드로부터의 최단 경로, 노드 번호)
queue = []

# 시작 노드에 대한 정보 초기화
heapq.heappush(queue, (0, start))
distance[start] = 0

# 우선순위 큐가 빌 때까지 수행
while queue:
    # 최단 경로를 갖는 노드 정보 가져오기
    cost, node = heapq.heappop(queue)

    # 현재 노드가 이미 처리된 노드인 경우
    if distance[node] < cost:
        # 건너 뛰기
        continue
    
    # 현재 노드에 대한 연결 노드 확인
    for linkedNode, linkedCost in graph[node]:
        # 해당 노드를 거쳐 이동하는 비용
        linkedCost = cost + linkedCost

        # 최단 거리 갱신
        if linkedCost < distance[linkedNode]:
            distance[linkedNode] = linkedCost
            heapq.heappush(queue, (linkedCost, linkedNode))

# ****** 출력 ****** #

# 시작 노드에서 출발하여
# 다른 모든 노드에 도착하는데
# 걸리는 최단 거리를
# 모두 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, INF 출력
    if distance[i] == INF:
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

# 출력
# 0
# 2
# 3
# 1
# 2
# 4