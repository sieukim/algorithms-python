from distutils.errors import LinkError
import heapq


INF = int(1e9)

# N: 도시 개수, M: 통로 개수, C: 메세지를 보내고자 하는 도시
n, m, start = map(int, input().split())

# 최단 거리 테이블
distance = [INF] * (n + 1)

# graph: 각 노드에 대한 연결 노드 정보를 담는 리스트
graph = [[]for _ in range(n + 1)]

for _ in range(m):
    # X: 출발 도시
    # Y: 도착 도시
    # Z: 메세지 전달 시간
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 우선순위 큐
queue = []
# 출발 노드 정보 초기화
heapq.heappush(queue, (0, start))
distance[start] = 0

while queue:
    # 최단 거리를 갖는 노드 정보 가져오기
    dist, node = heapq.heappop(queue)
    # 기존 최단 거리보다 큰 경우
    if distance[node] < dist:
        # 건너 뛰기
        continue
    # 현재 노드와 인접한 노드 확인
    for linkedNode, linkedDist in graph[node]:
        linkedDist += dist
        # 최단 거리 갱신
        if linkedDist < distance[linkedNode]:
            distance[linkedNode] = linkedDist
            heapq.heappush(queue, (linkedDist, linkedNode))
    
# 도달하는 노드 개수
count = 0
# 도달하는 노드 중, 가장 멀리 있는 노드와의 최단 거리
max_dist = 0

for dist in distance:
    # 도달할 수 있는 노드인 경우
    if dist != INF:
        count += 1
        max_dist = max(max_dist, dist)

print(count - 1, max_dist)

# 예제 1
#
# 입력
# 3 2 1
# 1 2 4
# 1 3 2
#
# 출력
# 2 4
