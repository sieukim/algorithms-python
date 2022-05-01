# 0과 1로만 이루어진 문자열 -> 정수형 리스트
numbers = list(map(int, list(input())))

# [0으로 이루어진 부분 문자열 개수, 
#    1로 이루어진 부분 문자열 개수]
substr = [0, 0]

# 첫 부분 문자열에 대한 초기화
substr[numbers[0]] += 1

for i in range(1, len(numbers)):
    # 새로운 부분 문자열이 시작된 경우
    if numbers[i] != numbers[i - 1]:
        substr[numbers[i]] += 1

# 정답 = 최소 부분 문자열 개수
print(min(substr))

# 예제1
#
# 입력
# 0001100
# 
# 출력
# 1