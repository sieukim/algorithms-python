def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 노드와 간선의 개수
v, e = map(int, input().split())
# 부모 테이블
parent = [i for i in range(v + 1)]

# 간선 리스트
edges = []
# 유지 비용 
result = 0

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용을 기준으로 오름차순 정렬
edges.sort()
# 최대 비용 
max_cost = 0

for edge in edges:
    cost, a, b = edge
    # 사이클이 존재하지 않는 경우
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

# 2개의 최소 신장 트리를 만들기 위해 
# 하나의 최소 신장 트리를 만들고
# 그 중 최대 비용 간선을 제거 
print(result - max_cost)

# 예제 1
#
# 입력
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
#
# 출력
# 8