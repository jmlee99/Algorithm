# 위에서 아래로
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()
array.reverse()
# sorted(array, reverse = True)

for i in array:
    print(i, end = ' ')

