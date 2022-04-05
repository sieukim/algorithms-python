# function that convert from input into integer list
def convert(input):
    return list(map(int, input.split(' ')))

# get N, M
n, m = map(int, input().split(' '))
# get card matrix
cards = [convert(input()) for i in range(n)]
# get minimum values of each rows
minValues = list(map(lambda x: min(x), cards))
# print answer (maximum value of minimum values)
print(max(minValues))


# 예제 1
#
# 입력 
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력
# 2

# 예제 2
#
# 입력 
# 2 4
# 7 3 1 8
# 3 3 3 4
#
# 출력
# 3