# 동전 개수
n = int(input())

# 각 동전의 화폐 단위 리스트
units = list(map(int, input().split()))

# 오름차순 정렬
units.sort()

target = 1

for unit in units:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < unit:
        break
    target += unit

print(target)

# 예제1
#
# 입력
# 5
# 3 2 1 1 9
# 
# 출력
# 8

# 예제2
#
# 입력
# 3
# 3 5 7
#
# 출력
# 1