# n from stdin
n = int(input())

# 정답을 나누는 수
divisor = 796796

# dp table
# dp[i]: 가로 길이 i를 채우는데 필요한 타일의 개수
# dp[0]: 사용 x
dp = [0] * 1001

# 가로 길이 1을 채우는데 필요한 타일: 1 x 2 한개 사용
dp[1] = 1 
# 가로 길이 2를 채우는데 필요한 타일: 1 x 2 두개 사용, 2 x 1 두개 사용, 2 x 2 한개 사용
dp[2] = 3

for i in range(3, n + 1):
    # 가로 길이 i를 채우는데 필요한 타일
    # = 가로 길이 i - 2를 채우는데 필요한 타일 * (2 x 1 두개 사용, 2 x 2 한개 사용) (1 x 2 두개 사용은 아래 케이스랑 중복되므로 고려 x)
    # + 가로 길이 i - 1를 채우는데 필요한 타일 * (1 x 2 두개 사용)
    dp[i] = dp[i - 2] * 2 + dp[i - 1]
    # 오버플로우 대비 매 계산 나머지 연산 수행
    dp[i] %= divisor

print(dp[n])

# 예제 1
#
# 입력
# 3
#
# 출력
# 5