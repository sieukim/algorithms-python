# get N, K
import math


n, k = map(int, input().split(' '))

# the number of executing rule 1
count1 = n % k
# the number of executing rule 2
count2 = math.log(n - count1, k)
# answer 
answer = int(count1 + count2)
print(answer)


# 예제 1
#
# 입력 
# 25 5
#
# 출력
# 2

# 예제 2
#
# 입력 
# 17 4
#
# 출력
# 3