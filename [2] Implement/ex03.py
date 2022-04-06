# function that convert from input into integer list
def convert(input):
    return list(map(int, input.split(' ')))

# n, m from STDIN
n, m = convert(input())
# current coordinate(y, x) and direction(d, 0: 북, 1: 동, 2: 남, 3: 서) from STDIN
y, x, d = convert(input())
# d 값 바꾸기 (0: 북, 1: 서, 2: 남, 3: 동)
d = ((d - 4) * -1) % 4
# map's information from STDIN (0: 육지, 1: 바다)
map = [convert(input()) for i in range(n)]

# 현재 방향에 대한 [왼쪽 방향, 현재 좌표와 왼쪽 방향 좌표와의 차이(y, x)] 리스트, 현재 방향 기준 북서남동 순서
left = [[1, 0, -1], [2, 1, 0], [3, 0, 1], [0, -1, 0]]
# 현재 방향에 대한 [현재 좌표와 뒤쪽 방향 좌표와의 차이(y, x)] 리스트, 현재 방향 기준 북서남동 순서
back = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 움직일 수 없을 때까지 테스트
while True:
    # 현재 위치 체크 (방문: 2, 바다: 1, 땅: 0)
    map[y][x] = 2
    # 이동 여부
    moved = False
    # 왼쪽 방향 체크
    for i in range(4):
        # [왼쪽 방향, 현재 좌표와 왼쪽 방향 좌표와의 차이(y, x)]
        [leftD, leftY, leftX] = left[(d + i) % 4]
        # 왼쪽 방향 좌표에 가본 적 없는 경우
        if map[y + leftY][x + leftX] == 0:
            # 이동
            y += leftY
            x += leftX
            moved = True
            # 방향 변경
            d = leftD
            # 왼쪽 방향 체크 중단
            break
    # 이동을 못 한 경우
    if moved == False:
        # [현재 좌표와 뒤쪽 방향 좌표와의 차이(y, x)] 
        [backY, backX] = back[d]
        # 뒤쪽 방향으로 갈 수 없는 경우
        if map[y + backY][x + backX] > 0:
            # 현재 위치에서 테스트 종료
            break
        # 뒤쪽 방향으로 갈 수 있는 경우
        else:
            # 뒤쪽 방향으로 이동
            y += backY
            x += backX

# 정답
answer = sum([row.count(2) for row in map])
# 정답 출력
print(answer)

# 예제 1
#
# 입력 
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1 
#
# 출력
# 3

