# -*- coding: utf-8 -*-

# n from STDIN
n = input()

# 정답
answer = 0

for i in range(n + 1):
    # i시 00분 00초 ~ i시 59분 59초 중 3을 하나라도 포함하는 경우의 수
    # 3시 또는 13시, 23시인 경우, 모든 경우의 수
    if i == 3 or i == 13 or i == 23:
        answer += 6 * 10 * 6 * 10
    # 그 외 시간인 경우, 모든 경우의 수 - 3이 안 들어가는 경우의 수
    else:
        answer += 6 * 10 * 6 * 10 - 5 * 9 * 5 * 9

# 정답 출력
print(answer)

# 예제 1
#
# 입력 
# 5
#
# 출력
# 11475

