#왕실의 나이트

data = input()
row = int(data[1])
# column의 a라는 문자를 유니코드로 변환 시키고 최종적으로 숫자로 만들어 내는 것
col = int(ord(data[0])) - int(ord('a')) + 1 # 1

steps = [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0

for step in steps:
    # 이동하고자 하는 다음 위치를 확인
    row_next = row + step[0]
    col_next = col = step[1]
    # 이동하고자 하는 다음 위치가 8x8을 벗어 나지 않는 지 확인
    if (row_next >= 1) & (row_next <= 8) & (col_next >= 1) & (col_next <= 8):
        count += 1

print(count)
