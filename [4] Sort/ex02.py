# n from stdin
n = int(input())
# student info from stdin
students = [input().split(' ') for i in range(n)]

# 점수를 기준으로 내림차순 정렬
students = sorted(students, key=lambda x: x[1])

# 정답 출력
for student in students:
    # 이름만 출력
    print(student[0], end=' ')


# 예제 1
#
# 입력 
# 2
# 홍길동 95
# 이순신 77
#
# 출력
# 이순신 홍길동