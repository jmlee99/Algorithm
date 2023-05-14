# 1260원을 거슬러 줄 때 최소 동전의 갯수는 ?

n = 1260
count = 0

list1 = [500, 100, 50, 10]

for i in list1:
    count += n//i
    n %= i

print(count)

