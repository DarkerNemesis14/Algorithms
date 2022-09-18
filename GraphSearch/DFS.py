seq = []
visit = []
def DFS(graph: list, node) -> list:
    seq.append(node)
    visit.append(node)
    for node in graph[seq[-1]]:
        if node not in visit:
            DFS(graph, node)
    return seq