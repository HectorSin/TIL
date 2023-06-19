8장 [그래프]

# 그래프의 추상 자료형

### GRAPH ADT

- IsEmpty():
- countVertex(): 정점의 수 반환
- countEdge(): 간선의 수 반환
- getEdge(u,v): 정점 u에서 정점 v로 연결된 간선을 반환
- degree(v): 정점 v의 차수를 반환
- adjacent(v): 정점 v에 인접한 모든 정점의 집합을 반환
- insertVertex(v): 그래프에 정점 v를 삽입
- insertEdge(u,v): 그래프에 간선 (u,v)를 삽입
- deleteVertex(v): 그래프의 정점 v를 삭제
- deleteEdge(v): 그래프의 간선 (u,v)를 삭제

### 깊이 우선 탐색 알고리즘

> 깊이 우선 탐색은 한 정점에서 시작하여 최대한 깊숙히 탐색하면서 진행
> 현재 정점에서 갈 수 있는 경로를 모두 탐색한 후 다음 결로로 이동
> 후입선출(LIFO) 구조의 스택을 사용하여 탐색 경로를 관리

def dfs(graph, start, visited = set()):

### 너비 우선 탐색 알고리즘

> 한 정점에서 시작하여 인접한 정점들을 우선적으로 탐색
> 현재 정점에서 인접한 정점들을 모두 탐색한 후 다음 단계로 이동
> 큐(Queue)를 사용하여 구현가능
> 선입선출(FIFO)구조의 큐를 사용하여 탐색 경로를 관리
> 주로 최단 경로 찾기, 네트워크 분석, 그래프의 최단 경로 등에 사용

def bfs(graph, start):

### 연결 성분 검사 알고리즘

> 그래프의 임의의 정점을 선택하고, DFS를 통해 연결되어 잇는 모든 정점들을 출력
> 더이상 연결된 정점이 없으면 그래프에서 아직 방문하지 않은 다른 정점을 선택해 동일 과정을 수행
> 그래프의 모든 정점을 방문할 때까지 반복

def find_connected_component(graph):

def dfs_cc(graph, color, vertex, visited):

### 신장 트리 알고리즘

def bfsST(graph, start):

### 위상 정렬 알고리즘

def topological_sort_AM(vertex, graph):
