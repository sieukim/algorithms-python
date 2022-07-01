# 두 원소가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 노드와 간선의 개수
v, e = map(int, input().split())

# 부모 테이블
parent = [i for i in range(0, v + 1)]

# union
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')



# 예제 1
#
# 입력
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
#
# 출력
# 각 원소가 속한 집합: 1 1 1 1 5 5
# 부모 테이블: 1 1 1 1 5 5