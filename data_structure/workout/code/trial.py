from l10_graph import bfsST, find_connected_component, topological_sort_AM

# 그래프를 인접 리스트로 표현합니다.
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D']),
    'C': set(['A', 'E']),
    'D': set(['B']),
    'E': set(['C', 'F']),
    'F': set(['E'])
}
# 연결 성분 검사 알고리즘
find_connected_component(graph)
print()

# 신장 트리 알고리즘
bfsST(graph, 'A')
print()

# 위상 정렬 알고리즘용 테스트 데이터
vertex = ['A', 'B', 'C', 'D', 'E', 'F']
graphAM = [[0, 0, 1, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0]]
print('topological_sort')
# 위상 정렬 알고리즘
topological_sort_AM(vertex, graphAM)
print()

from l11_wGraph import weightSum, printAllEdges

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, 22, None, 18],
          [None, None, None, 22, None, 27, 25],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]

graph = (vertex, weight)

# 인접 행렬: 간단한 연산
print('AM: weight sum = ',weightSum(vertex, weight))

print()

# 인접 행렬에서의 모든 간선 출력
printAllEdges(vertex, weight)

### 인접 리스트를 이용한 표현

graph = {'A': set([('B',29),('F',10)]),
         'B': set([('A',29),('C',16), ('G',15)]),
         'C': set([('B',16),('D',12)]),
         'D': set([('C',12),('E',22),('G',18)]),
         'E': set([('D',22),('F',27),('G',25)]),
         'F': set([('A',10),('E',27)]),
         'G': set([('B',15),('D',18),('E',25)])}


### union-find 구현

### Kruskal 알고리즘의 구현

### Prim의 알고리즘

### Dijkstra 최단경로 알고리즘

### Floyd의 최단 경로 알고리즘