# 11장 가중치그래프

### 인접 행렬을 이용한 표현

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, 22, None, 18],
          [None, None, None, 22, None, 27, 25],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]

graph = (vertex, weight)

### 인접 행렬: 간단한 연산

# 매개변수: 정점 리스트, 인접 행렬
def weightSum(vlist, W):
    sum = 0
    for i in range(len(vlist)):
        for j in range(i+1, len(vlist)):
            if W[i][j] != None:
                sum += W[i][j]
    return sum

# 매개변수: 정점 리스트, 인접 행렬
def printAllEdges(vlist, W):
    for i in range(len(vlist)):
        # 모든 간선 W[i][j]에 대해
        for j in range(i+1, len(W[i])):
            # 간선이 있으면
            if W[i][j] != None and W[i][j] != 0:
                print("(%s,%s,%d)"%(vlist[i], vlist[j], W[i][j]), end= ' ')
    print()

### 인접 리스트를 이용한 표현

# 가중치의 총 합을 구하는 함수
def weightSum(graph):
    sum = 0
    # 그래프의 모든 정점 v에 대해: 'A', 'B', ...
    for v in graph:
        # v의 모든 간선 e에 대해: ('B', 29), ...
        for e in graph[v]:
            # sum에 추가
            sum += e[1]
    # 하나의 간선이 두 번 더해지므로 2로 나눔
    return sum//2

# 가중치의 총 합을 구하는 함수
def weightSum(graph):
    sum = 0
    # 그래프의 모든 정점 v에 대해: 'A', 'B', ...
    for v in graph:
        # v의 모든 간선 e에 대해: ('B', 29), ...
        for e in graph[v]:
            # sum에 추가
            sum += e[1]
    # 하나의 간선이 두 번 더해지므로 2로 나눔
    return sum//2

# 모든 간선을 출력하는 함수
def printAllEdges(graph):
    # 그래프의 모든 정점 v에 대해: 'A', 'B', ...
    for v in graph:
        # v의 모든 간선 e에 대해: ('B', 29), ...
        for e in graph[v]:
            print("(%s, %s, %d)"%(v,e[0],e[1]), end=' ')

### union-find 구현

### Kruskal 알고리즘의 구현

### Prim의 알고리즘

### Dijkstra 최단경로 알고리즘

### Floyd의 최단 경로 알고리즘