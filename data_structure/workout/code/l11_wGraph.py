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

### union-find 구현

### Kruskal 알고리즘의 구현

### Prim의 알고리즘

### Dijkstra 최단경로 알고리즘

### Floyd의 최단 경로 알고리즘