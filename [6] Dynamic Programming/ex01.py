# x from stdin
x = int(input())

# dp table
dp = [0] * 30001

# dp (bottom-up)
for i in range(2, x + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 2로 나누어 떨어지는 경우 => 2로 나눈 값을 구하는 연산 횟수 + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우 => 3으로 나눈 값을 구하는 연산 횟수 + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 5로 나누어 떨어지는 경우 => 5로 나눈 값을 구하는 연산 횟수 + 1
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])


# 예제 1
#
# 입력
# 26
#
# 출력
# 3