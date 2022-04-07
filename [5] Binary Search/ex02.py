import sys

# convert input into integer list
def convert(input):
    return list(map(int, input))

# 잘린 떡 길이 리스트
def cut(riceCakes, height):
    return [riceCake - height if riceCake > height else 0 for riceCake in riceCakes]

# n, m from stdin
[n, m] = convert(sys.stdin.readline().rstrip().split(' '))
# riceCakes(list) from stdin
riceCakes = convert(sys.stdin.readline().rstrip().split(' '))

# 정답
answer = 0

# 최대 절단기 높이를 탐색 (이진 탐색, 범위: 0 ~ 떡 길이 최대값)
start = 0
end = max(riceCakes)

while start <= end:
    # 중간값
    mid = (start + end) // 2
    # 절단기 높이가 mid일 때, 잘린 떡 길이 합
    cutSum = sum(cut(riceCakes, mid))
    # 잘린 떡 길이 합이 요청한 떡의 길이 m과 같은 경우
    if cutSum == m:
        # 탐색 종료
        answer = mid
        break
    # m보다 큰 경우
    if cutSum > m:
        # 절단기 높이 증가
        start = mid + 1 
    # m보다 큰 경우
    else:
        # 절단기 높이 감소
        end = mid - 1

# 정답 출력
print(answer)


# 예제 1
#
# 입력
# 4 6
# 19 15 10 17
#
# 출력
# 15