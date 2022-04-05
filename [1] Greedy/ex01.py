# function that convert from input into integer list
def convert(input):
    return list(map(int, input.split(' ')))

# N, M, K from Stdin
[N, M, K] = convert(input())
# integer list from Stdin
integerList = convert(input())
# sort by descending
integerList = sorted(integerList, reverse=True)

# calculate sum of pattern (integerList[0] * k + integerList[1] * 1)
patternSum = integerList[0] * K + integerList[1] * 1
# calculate the number of pattern
patternCount = M // (K + 1)
# calculate the number of mod(rested)
patternRested = M % (K + 1)

# answer(sum)
answer = patternSum * patternCount + integerList[0] * patternRested
print(patternSum, patternCount, patternRested)
# print answer
print(answer)

# 예제 1
#
# 입력 
# 5 8 3
# 2 4 5 4 6
#
# 출력
# 46

# 예제 2
#
# 입력 
# 5 7 2
# 3 4 3 4 3
#
# 출력
# 28