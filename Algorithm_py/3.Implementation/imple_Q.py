# 구현

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
# 실질적으로 오른쪽, 왼쪽으로 이동하면 y의 좌표가 바뀌고, 위, 아래로 이동하면 x의 좌표가 바뀐다.
# 즉 그래프로 생각하지말고, 행이 x, 열이 y라 생각하자.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 찍기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny <1 or  nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

