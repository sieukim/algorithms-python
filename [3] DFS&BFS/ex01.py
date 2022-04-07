# function that convert from input into integer list
def convert(input):
    return list(map(int, input.split(' ')))

# dfs: graph[y][x] 방문
def dfs(y, x):
    # 유효 범위가 아닌 경우
    if y < 0 or y >= n or x < 0 or x >= m:
        return False
    # 0인 경우(방문 x)
    if graph[y][x] == '0':
        # 방문 처리
        graph[y][x] = '1'
        # 상
        dfs(y - 1, x)
        # 하
        dfs(y + 1, x)
        # 좌
        dfs(y, x - 1)
        # 우
        dfs(y, x + 1)
        # True 반환
        return True
    # 1인 경우
    else:
        return False

# n, m from stdin
[n, m] = convert(input())
# graph from stdin
graph = [list(input()) for i in range(n)]

# 정답
answer = 0

# 모든 노드에 대해 dfs 함수 호출
for i in range(n):
    for j in range(m):
        # print(dfs(i, j), answer)
        if dfs(i, j) == True:
            answer += 1

# 정답 출력
print(answer)


# 예제 1
#
# 입력 
# 4 5
# 00110
# 00011
# 11111
# 00000
#
# 출력
# 3

# 예제 2
#
# 입력 
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
#
# 출력
# 8

