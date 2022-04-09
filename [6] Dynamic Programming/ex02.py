# N from stdin
n = int(input())
# food inventory from stdin
inventory = list(map(int, input().split(' ')))

# dp table
# dp[i]: i번째 식량창고까지 약탈할 때 얻을 수 있는 식량의 최대값
dp = [0] * n

dp[0] = inventory[0]
dp[1] = max(inventory[0], inventory[1])

for i in range(2, n):
    # dp[i - 1]: i번째 식량 창고 약탈 x
    # dp[i - 2] + inventory[i]: i번째 식량 창고 약탈 o
    # 둘 중 더 큰 값을 골라 i번째 식량 창고 약탈 여부를 고름
    dp[i] = max(dp[i - 1], dp[i - 2] + inventory[i])

print(dp[n - 1])


# 예제 1
#
# 입력
# 4
# 1 3 1 5
#
# 출력
# 8