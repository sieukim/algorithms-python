# coordinate(x, y) from STDIN
[x, y] = list(input())

# a ~ h 값을 0 ~ 7 으로 변환
x = ord(x) - 97
# 1 ~ 8 값을 0 ~ 7 으로 변환
y = int(y) - 1

# 정답
answer = 0

# 나이트 이동 방향(8가지)
steps = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

# 모든 이동 방향에 대하여 유효한 경우인지 확인
for step in steps:
    # x 좌표 범위를 넘은 경우
    if x + step[0] < 0 or x + step[0] > 7:
        continue
    # y 좌표 범위를 넘은 경우
    if y + step[1] < 0 or y + step[1] > 7:
        continue
    # 모든 범위를 맞춘 경우
    answer += 1

# 정답 출력
print(answer)

# 예제 1
#
# 입력 
# a1
#
# 출력
# 2

# 예제 2
#
# 입력 
# c2
#
# 출력
# 6

