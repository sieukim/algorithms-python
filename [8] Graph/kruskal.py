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
parent = [i for i in range(v+1)]

# 간선 리스트
edges = []
# 최종 비용
result = 0

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용을 기준으로 오름차순 정렬
edges.sort()

# kruskal
for edge in edges:
    cost, a, b = edge
    # 사이클 여부 확인
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b) 
        result += cost

print(result)

# 예제 1
#
# 입력
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
#
# 출력
# 159