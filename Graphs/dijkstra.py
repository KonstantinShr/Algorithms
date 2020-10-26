INF = 1000000000


# GRAPH IS A ADJACENCY MATRIX
def dijkstra(graph, v, finish):
    dist = 0
    way = []
    while dist < INF:
        way.append(v)
        if min(graph[v]) == INF:
            break
        if min(graph[v]) != graph[v][finish]:
            dist += min(graph[v])
            for j in range(len(graph)):
                graph[j][v] = INF
            v = graph[v].index(min(graph[v]))
        else:
            dist += min(graph[v])
            way.append(finish)
            print(way)
            return dist
    return "The way doesn't found"


# EXAMPLE
graph = [[INF, 5, 10, INF, 2, INF],
         [5, INF, 2, 4, INF, INF],
         [10, 2, INF, 4, INF, 10],
         [INF, 4, 7, INF, 3, INF],
         [2, INF, INF, 3, INF, INF],
         [INF, INF, 10, INF, INF, INF]]

