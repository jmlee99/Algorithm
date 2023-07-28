# 시각
# 완전 탐색 유형이다.
# 단순히 하루는 86400초이다. 이것을 모든 경우의 수를 돌면서 새면 된다.
n = int(input())
count = 0
for i in range(n + 1):
    for e in range(60):
        for j in range(60):
            if '3' in str(i) + str(e) + str(j):
                count += 1

print(count)
