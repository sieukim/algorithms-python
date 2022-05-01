from curses.ascii import isalpha

# 문자열 s
s = input()

# 문자열 s 내 알파벳 리스트
alpha = [value for value in s if isalpha(value) == True ]
# 문자열 s 내 정수 리스트
number = [int(value) for value in s if isalpha(value) != True ]

# 알파벳 오름차순 정렬
alpha.sort()

# 정렬된 알파벳 리스트에 정수 합 추가
alpha.append(str(sum(number)))

# 정답 출력
print("".join(alpha))

# 예제 1
#
# 입력
# K1KA5CB7
#
# 출력
# ABCKK13

# 예제 2
#
# 입력
# AJKDLSI412K4JSJ9D
#
# 출력
# ADDIJJJKKLSS20