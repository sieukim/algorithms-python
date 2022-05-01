# n: 볼링공 개수, m: 공의 최대 무게
n, m = map(int, input().split())

# 각 볼링공 무게 리스트
weights = list(map(int, input().split()))

# 오름차순 정렬
weights.sort()

# ball[i]: 무게가 i인 볼링골 개수
ball = [weights.count(i) for i in range(0, 11)]

# 두 사람이 볼링공을 고르는 경우의 수(정답)
count = 0

for i in range(11):
    # 무게가 1인 볼링골의 개수 
    # * 무게가 i인 볼링골을 제외한 볼링골의 개수 
    count += ball[i] * (n - ball[i])

# 정답 출력 (조합이므로 2로 나눔)
print(count / 2)

# 예제 1
#
# 입력
# 5 3
# 1 3 2 3 2
#
# 출력
# 8

# 예제 2
#
# 입력
# 8 5
# 1 5 4 3 2 4 5 2
#
# 출력
# 25