from bisect import bisect
import sys

# convert input into integer list
def convert(input):
    return list(map(int, input))

# n from stdin
n = int(sys.stdin.readline().rstrip())
# list from stdin
listN = convert(sys.stdin.readline().rstrip().split(' '))
# m from stdin
m = int(sys.stdin.readline().rstrip())
# list from stdin
listM = convert(sys.stdin.readline().rstrip().split(' '))

# 오름차순 정렬
listN.sort()

# 정답
answer = ''

for value in listM:
    # bisect(a, x): a에 있는 x의 기존 항목 뒤(오른쪽)에 오는 삽입 위치를 반환
    index = bisect(listN, value)
    # index의 왼쪽 값이 value인 경우 => 존재
    if listN[index - 1] == value:
        answer += 'yes '
    # index의 왼쪽 값이 value가 아닌 경우 => 존재 x
    else:
        answer += 'no '

# 정답 출력
print(answer.rstrip())

# 예제 1
#
# 입력
# 5
# 8 3 7 9 2
# 3
# 5 7 9
#
# 출력
# no yes yes