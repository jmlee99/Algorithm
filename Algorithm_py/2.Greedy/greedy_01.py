# 숫자 카드 게임
# 내 답안
n, m = map(int, input().split())

min_value = []
for i in range(n):
    data = list(map(int, input().split()))
    min_value.append(min(data))

print(max(min_value))

# 정답안
# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

