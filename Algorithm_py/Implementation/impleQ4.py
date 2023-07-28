# 게임 개발
# 전체 맵 입력 받기
n, m = map(int, input().split())

# 방문한 위치를 저장할 맵 생성
d = [[0] * m for _ in range(n)]

# 현재의 위치와 현재 바라보는 방향 입력
x, y, direct = map(int, input().split())
# 현재 서 있는 곳은 방문한 것으로 설정
d[x][y] = 1

# 전체 맵의 정보를 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# d_row, d_col 설정
# 북, 동, 남, 서
d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

count = 1 # 현재 서 있는 곳을 1로 했으니 초기값은 1
turn_time = 0

while True:
    turn_left()
    n_row = x + d_row[direct]
    n_col = y + d_col[direct]
    if d[n_row][n_col] == 0 and array[n_row][n_col] == 0: # 회전한 이후 정면이 가보지 않은 곳이 존재할 경우
        d[n_row][n_col] = 1
        x = n_row
        y = n_col
        count += 1
        turn_time = 0
        continue
    else: # 회전 후 정면이 가본 곳이거나 바다인 경우
        turn_time += 1
    # 모든 방향이 갈 수 없는 경우
    if turn_time == 4:
        n_row = x - d_row[direct]
        n_col = y - d_col[direct]
        turn_time = 0
        #뒤로 갈 수 있으면
        if array[n_row][n_col] == 0:
            x = n_row
            y = n_col
        # 뒤가 바다이면
        else:
            break

print(count)

#이 문제는 언제 끝나는지가 중요 언제 끝나는지 기준을 잡고 그에 맞춰가면서 코드를 짜나가야한다.