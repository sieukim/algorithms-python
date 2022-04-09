# n, m from stdin
n, m = list(map(int, input().split(' ')))
# units from stdin
units = [int(input()) for _ in range(n)]

# dp table
# dp[i]: i원을 만들기 위한 최소한의 화폐 개수
dp = [0] * (m + 1)

# 최소 단위
minUnit = min(units)

# 최소 단위 금액을 만드는 방법은 한가지
dp[minUnit] = 1

for i in range(minUnit, m + 1):
    # i원을 만들기 위한 최소한의 화폐 개수
    # = (i - 각 화폐 단위)원을 만들기 위한 최소한의 화폐 개수의 최소값 + 1
    
    # (i - 각 화폐 단위)원을 만들기 위한 최소한의 화폐 개수 리스트
    counts = [dp[i - unit] for unit in units if i >= unit and dp[i - unit] != 0]

    # (i - 각 화폐 단위)원을 만드는 경우의 수가 있는 경우
    if len(counts) > 0:
        dp[i] = min(counts) + 1
    # (i - 각 화폐 단위)원을 만드는 경우의 수가 없더라도 i원이 화폐 단위에 속하는 경우
    elif i in units:
        dp[i] = 1
    # i원을 못 만드는 경우
    else:
        dp[i] = 0


print(dp[m] if dp[m] > 0 else -1)


# 예제 1
#
# 입력
# 2 15
# 2
# 3
#
# 출력
# 5

# 예제 2
#
# 입력
# 3 4
# 3
# 5
# 7
#
# 출력
# -1