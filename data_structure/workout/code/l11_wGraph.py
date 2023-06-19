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

# 각 노드의 부모노드 인덱스
parent = []
# 전체 집합의 개수
set_size = 0

# 집합의 초기화 함수: 모든 정점들을 각각 고유의 집합으로 설정
def init_set(nSets):
    # 전역변수 사용(변경)을 위함
    global set_size, parent
    # 집합의 개수
    set_size = nSets
    # 모든 집합에 대해
    for i in range(nSets):
        # 각각이 고유의 집합(부모가 -1)
        parent.append(-1)

# 정점 id가 속한 집합의 대표번호 탐색
def find(id):
    # 부모가 있는 동안(-1이 아닌 동안)
    while(parent[id] >= 0):
        # id를 부모 id로 갱신
        id = parent[id]
    # 최종 id 반환, 트리의 맨 위 노드의 id임
    return id

# 두 집합을 병합(s1을 s2에 병합시킴)
def union(s1, s2):
    # 전역변수 사용을 위함
    global set_size
    # s1을 s2에 병합시킴
    parent[s1] = s2
    # 집합의 개수가 줄어 듦
    set_size = set_size - 1

### Kruskal 알고리즘의 구현

### Prim의 알고리즘

### Dijkstra 최단경로 알고리즘

### Floyd의 최단 경로 알고리즘