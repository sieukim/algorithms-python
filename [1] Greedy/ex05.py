# 문자열 -> 정수형 리스트
numbers = list(map(int, list(input())))

# 결과 (정답)
result = 0

for number in numbers:
    # 더하기 연산 또는 곱하기 연산을 수행해 
    # 더 큰 값이 나오는 것을 선택
    result = max([result + number, result * number])

# 정답 출력
print(result)

# 예제1
#
# 입력
# 02984
# 
# 출력
# 576

# 예제2
#
# 입력
# 567
# 
# 출력
# 210