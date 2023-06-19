from l8_tree import dfs

# 그래프를 인접 리스트로 표현합니다.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

dfs(graph, 'A')