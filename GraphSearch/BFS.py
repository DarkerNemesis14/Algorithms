def BFS(graph: dict, source) -> list:
    queue, seq, visit = [source], [], [source]
    while queue:
        seq.append(queue.pop(0))
        for node in graph[seq[-1]]:
            if node not in visit:
                queue.append(node)
                visit.append(node)
    return seq