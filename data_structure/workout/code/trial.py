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
