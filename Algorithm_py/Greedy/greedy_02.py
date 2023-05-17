# 내 답안

n, k = map(int, input().split())

count = 0
# 따로 반복돌 횟수가 정해지지 않았기 때문에 일단 무한반복구문
while True:
    if n%k == 0:
        n //= k
        count += 1
        if n == 1:
            break
    else:
        n -= 1
        count += 1
        if n == 1:
            break

print(count)

# 책 답안
n, k = map(int, input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)