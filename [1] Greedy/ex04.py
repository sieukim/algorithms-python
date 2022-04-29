# N: 모험가 수
n = int(input())
# 각 모험가의 공포도 리스트
adventurers = list(map(int, input().split()))

# 오름차순 정렬
adventurers.sort()

# 여행을 떠날 수 있는 그룹 수(정답)
answer = 0

# 현재 그룹 내 모험가의 수 
count = 0

for adventurer in adventurers:
    # 현재 그룹 내 모험가의 수가 
    # 현재 모험가의 공포도 미만인 경우
    # => 현재 그룹에 추가
    if count < adventurer:
        count += 1
    # 현재 그룹 내 모험가의 수가
    # 현재 모험가의 공포도와 같은 경우
    # => 현재 그룹 종료
    if count == adventurer:
        answer += 1
        count = 0
        
print(answer)

# 예제 1
#
# 입력 
# 5
# 2 3 1 2 2
#
# 출력
# 2
