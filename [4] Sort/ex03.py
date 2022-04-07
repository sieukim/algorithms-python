# convert input into integer list
def convert(input):
    return list(map(int, input))

# n, k from stdin
n, k = convert(input().split(' '))
# listA info from stdin
listA = convert(input().split(' '))
# listB info from stdin
listB = convert(input().split(' '))

# listA 오름차순 정렬
listA = sorted(listA)
# listB 내림차순 정렬
listB = sorted(listB, reverse=True)

# 최대 K번 수행
for i in range(k):
    # B의 요소가 더 큰 경우
    if listA[i] < listB[i]:
        # 교체
        listA[i], listB[i] = listB[i], listA[i]
    else:
        break

# 정답
answer = sum(listA)

# 정답 출력
print(answer)

# 예제 1
#
# 입력 
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
#
# 출력
# 26