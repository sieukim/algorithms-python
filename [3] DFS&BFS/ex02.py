from collections import deque

# function that convert from input into integer list
def convert(input):
    return list(map(int, input))

# bfs: [1, 1]부터 각 노드까지 걸리는 최단 거리를 기록하는 bfs
def bfs(y, x):
    # 네 방향 (상하좌우)
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # queue
    queue = deque()
    queue.append([y, x])

    while queue:
        # 최하위 위치
        [y, x] = queue.popleft()
        # 현재 방향에서 상하좌우 확인
        for direction in directions:
            # 이동량 
            [dy, dx] = direction
            # 범위를 넘은 경우
            if y + dy < 0 or y + dy >= n:
                continue
            if x + dx < 0 or x + dx >= m:
                continue
            # 벽인 경우
            if graph[y + dy][x + dx] == 0:
                continue
            # 처음 방문하는 노드인 경우
            if graph[y + dy][x + dx] == 1:
                graph[y + dy][x + dx] = graph[y][x] + 1
                queue.append([y + dy, x + dx])
    # [n, m]까지의 최단 거리
    return graph[n - 1][m - 1]

# n, m from stdin
[n, m] = convert(input().split(' '))
# graph from stdin
graph = [convert(input()) for i in range(n)]

# 정답
answer = bfs(0, 0)

# 정답 출력
print(answer)


# 예제 1
#
# 입력 
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
#
# 출력
# 10