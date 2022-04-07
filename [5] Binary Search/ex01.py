import sys

# convert input into integer list
def convert(input):
    return list(map(int, input))

# binary search
# 오름차순 정렬된 sortedList에서 target 위치 찾기
def binary_search(start, end, sortedList, target):
    # target의 위치
    index = -1

    while start <= end:
        # 중간값 인덱스
        mid = (start + end) // 2
        # 중간값
        midValue = sortedList[mid]
        # target이 중간값보다 작은 경우 -> 오른쪽으로 이동
        if target < midValue: 
            end = mid - 1
        # target이 중간값보다 큰 경우 -> 왼쪽으로 이동
        elif target > midValue:
            start = mid + 1
        # target이 중간값과 같은 경우 -> 탐색 종료
        else:
            index = mid
            break
    
    return index

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

binary_search(0, n - 1, listN, listM[0])

for value in listM:
    # value의 위치
    index = binary_search(0, n - 1, listN, value)
    # 존재하는 경우
    if index >= 0:
        answer += 'yes '
    # 존재하지 않는 경우
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