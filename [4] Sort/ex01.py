# n from stdin
n = int(input())
# numbers from stdin
numbers = [int(input()) for i in range(n)]

# 내림차순 정렬
numbers = sorted(numbers, reverse=True)

# 정답 출력
for number in numbers:
    print(number, end=' ')


# 예제 1
#
# 입력 
# 3
# 15
# 27
# 12
#
# 출력
# 27 15 12