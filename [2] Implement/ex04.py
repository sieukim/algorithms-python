# 점수 
score = list(map(int, list(input())))

# 점수 길이
n = len(score)

# 왼쪽 자릿수의 합
left = sum(score[:n//2])
# 오른쪽 자릿수의 합
right = sum(score[n//2:])

if left == right:
    print('LUCKY')
else:
    print('READY')


# 예제 1
#
# 입력
# 123402
#
# 출력
# LUCKY

# 예제 2
#
# 입력
# 7755
#
# 출력
# READY