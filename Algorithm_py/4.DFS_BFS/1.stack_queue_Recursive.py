# 스택 기초

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력 [5, 2, 3, 1]
print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]

# 큐 기초
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
"""
# 재귀함수 기초

def recursive():
    print('재귀함수를 호출합니다.')
    recursive()

recursive()
"""

# 재귀함수 종료 조건

def recursive_fun(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_fun(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_fun(1)


# 반복적으로 구현한 n!

def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n < 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))
