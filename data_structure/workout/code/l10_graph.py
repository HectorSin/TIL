# 그래프 클래스

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    # 그래프가 비어 있는지 확인 / 정점의 개수가 0이면 빈 그래프라고 반환
    def IsEmpty(self):
        return len(self.vertices) == 0
    
    #정점의 수 반환
    def countVertax(self):
        return len(self.vertices)
    
    # 간선의 개수 반환
    def countEdge(self):
        return len(self.edges)
    
    # 정점 u와 정점v 사이의 간선을 반환하는 메소드
    # 간선이 존재하지 않을 경우 None을 반환
    def getEdge(self, u, v):
        return self.edges.get((u,v))

    # 정점 v의 차수(인접한 정점의 개수)를 반환하는 메소드
    def degree(self, v):
        return len(self.vertices[v])
    
    # 정점 v에 인접한 모든 정점들의 집합을 반환하는 메소드
    def adjacent(self, v):
        return self.vertices[v]

    # 정점 v를 그래프에 삽입하는 메소드
    # 이미 그래프에 존재하는 정점인 경우 무시
    def insertVertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()

    # 정점 u와 정점 v를 연결하는 간선 (u, v)를 그래프에 삽입하는 메소드
    # 정점 u와 정점 v가 그래프에 존재하지 않는 경우 삽입하지 않고 False 반환
    def insertEdge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            return False
        
        self.vertices[u].add(v)
        self.vertices[v].add(u)
        self.edges[(u, v)] = True
        self.edges[(v, u)] = True
        return True

    # 정점 v와 연결된 간선들을 모두 삭제하고 정점 v를 그래프에서 삭제하는 메소드
    # 정점 v가 그래프에 존재하지 않는 경우 삭제하지 않고 False 반환
    def deleteVertex(self, v):
        if v not in self.vertices:
            return False
        
        adjacent_vertices = self.vertices[v]
        for u in adjacent_vertices:
            self.vertices[u].remove(v)
            del self.edges[(u, v)]
            del self.edges[(v, u)]

        del self.vertices[v]
        return True

    # 정점 u와 정점 v를 연결하는 간선 (u, v)를 그래프에서 삭제하는 메서드
    # 간선 (u,v)가 그래프에 존재하지 않는 경우 삭제하지 않고 False 반환
    def deleteEdge(self, u, v):
        if (u, v) not in self.edges:
            return False
        
        self.vertices[u].remove(v)
        self.vertices[v].remove(u)
        del self.edges[(u, v)]
        del self.edges[(v, u)]
        return True
    
# 깊이 우선 탐색(DFS)
def dfs(graph, start, visited = set()):
    # start가 방문하지 않은 정점이면
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

import collections

# 너비 우선 탐색 알고리즘(BFS)
def bfs(graph, start):
    # 맨 처음에는 start만 방문한 정점임
    visited = set([start])
    # 컬렉션의 덱 객체 생성(큐로 사용)
    queue = collections.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex, ene=' ')
        nbr = graph[vertex] - visited
        for v in nbr:
            visited.add(v)
            queue.append(v)

# 연결 성분 검사 알고리즘
def find_connected_component(graph):
    # 이미 방문한 정점 집합
    visited = set()
    # 부분 그래프별 정점 리스트
    colorList = []

    # 그래프의 모든 정점들에 대해
    for vtx in graph:
        # 방문하지 않은 정점이 있다면
        if vtx not in visited:
            # 새로운 컬러 리스트
            color = dfs_cc(graph, [], vtx, visited)
            # 컬러 리스트 추가
            colorList.append(color)

    print("그래프 연결성분 개수 = %d" %len(colorList))
    # 정점 리스트들을 출력
    print(colorList)

def dfs_cc(graph, color, vertex, visited):
    # 아직 칠해지지 않은 정점에 대해
    if vertex not in visited:
        # 이제 방문했음
        visited.add(vertex)
        # 같은 색의 정점 리스트에 추가
        color.append(vertex)
        # nbr: 차집합 연산 이용
        nbr = graph[vertex] - visited
        # v <- {인접정점}-{방문정점}
        for v in nbr:
            # 순환 호출
            dfs_cc(graph, color, v, visited)
        # 같은 색의 정점 리스트 반환
        return color
    
# 신장 트리 알고리즘
def bfsST(graph, start):
    # 맨 처음에는 start만 방문한 정점임
    visited = set([start])
    # 파이썬 컬렉션의 덱 생성(큐로 사용)
    queue = collections.deque([start])
    # 공백이 아닐 때 까지
    while queue:
        # 큐에서 하나의 정점 v를 빼냄
        v = queue.popleft()
        # nbr = {v의 인접정점} - {방문정점}
        nbr = graph[v] - visited
        # 갈 수 있는 모든 인접 정점에 대해
        for u in nbr:
            # (v,u)간선 추가
            print("(", v, ",", u, ")", end="")
            # 이제 u는 방문했음
            visited.add(u)
            # u를 큐에 삽입
            queue.append(u)
    
# 위상 정렬 알고리즘
def topological_sort_AM(vertex, graph):
    n = len(vertex)
    # 정점의 진입차수 저장
    inDeg = [0] * n

    for i in range(n):
        for j in range(n):
            # 인접 행렬로 표현한 그래프 이용
            if graph[i][j] > 0:
                # 진입차수를 1 증가시킴
                inDeg[j] += 1

    # 진입차수가 0인 정점 리스트를 만듦
    vlist = []
    for i in range(n):
        if inDeg[i]==0:
            vlist.append(i)

    # 리스트가 공백이 아닐 때 까지
    while len(vlist) > 0:
        # 진입차수가 0인 정점을 하나 꺼냄
        v = vlist.pop()
        # 화면 출력
        print(vertex[v], end=' ')

        for u in range(n):
            if v != u and graph[v][u] > 0:
                # 연결된 정점의 진입차수 감소
                inDeg[u] -= 1
                # 진입차수가 0이면
                if inDeg[u] == 0:
                    # vlist에 추가
                    vlist.append(u)