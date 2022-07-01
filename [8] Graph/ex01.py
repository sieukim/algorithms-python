# 팀 합치기 연산
def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 특정 학생이 속한 팀을 찾는 함수
def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]

# 같은 팀 여부 확인 연산
def check_team(parent, a, b):
    if find_team(parent, a) == find_team(parent, b):
        print('YES')
    else:
        print('NO')

# 노드와 간선의 개수
v, e = map(int, input().split())
# 부모 테이블
parent = [i for i in range(v + 1)]

# 간선 입력
for _ in range(e):
    op, a, b = map(int, input().split())
    # 팀 합치기
    if op == 0:
        union_team(parent, a, b)
    # 같은 팀 여부 확인
    else:
        check_team(parent, a, b)

# 예제 1
#
# 입력
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7 
# 0 4 2
# 0 1 1
# 1 1 1
#
# 출력
# NO
# NO
# YES