"""
    시간 복잡도 : 알고리즘을 위해 필요한 연산의 횟수
    공간 복잡도 : 알고리즘을 위해 필요한 메모리의 양

"""

# 가장 영향력이 큰 부분은 N에 비례하는 연산을 수행하는 반복문 부분이고 시간복잡도를 O(N = 5)이라고 표기한다.

array = [3, 5, 1, 2, 4] # 5개의 데이터 (N = 5)
summary = 0

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과를 출력
print(summary)

# ex1
a = 5
b = 7
print(a+b) # 시간복잡도는 O = 1이다  ( 대입연산과 출력연산을 제외하면 )

# ex2

array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i * j
        print(temp) # 여기서 시간복잡도는 = 25(N*N)이다.
