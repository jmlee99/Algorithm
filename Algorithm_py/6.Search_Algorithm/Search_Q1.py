# 부품 찾기
def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    re = binary_search(array, i, 0, n - 1)
    if re != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


for i in x:
    if i in array:
        print('yes', end = " ")
    else:
        print('no', end = ' ')


















