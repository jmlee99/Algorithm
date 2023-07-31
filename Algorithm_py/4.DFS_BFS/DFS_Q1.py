n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문

def dfs(row, col):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if (row <= -1) or (row >= n) or (col <= -1) or (col >= m):
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[row][col] == 0:
        # 해당노드 방문 처리
        graph[row][col] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 후출
        dfs(row-1, col) # 상
        dfs(row+1, col) # 하
        dfs(row, col-1) # 좌
        dfs(row, col+1) # 우
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0

for i in range(n):
    for e in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, e) == True:
            result += 1

print(result)