# 1260원을 거슬러 줄 때 최소 동전의 갯수는 ?

n = 1260
count = 0

list1 = [500, 100, 50, 10]

for i in list1:
    count += n//i
    n %= i

print(count) # 6


# 큰 수 법칙
# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()

st_1 = data[n - 1]
st_2 = data[n - 2]

result = 0
for i in range(m):
    if i != k | i != 2*k:
        result += st_1
    else:
        result += st_2


print(result)

# 답안 k를 반복문에 시간복잡도 낮춤

# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()

st_1 = data[n - 1]
st_2 = data[n - 2]

result = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # 반복문 탈출
            break
        result += st_1
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # 반복문 탈출
        break
    result += st_2
    m -= 1 # 더할 때마다 1씩 빼기

print(result)

# 답안 k를 반복문에 시간복잡도 낮춤

# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()

st_1 = data[n - 1]
st_2 = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * st_1
result += (m - count) * st_2

print(result)