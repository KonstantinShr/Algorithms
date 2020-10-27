INF = 1000000000


# GRAPH IS A ADJACENCY MATRIX
def prima(graph, v):
    vert_stack = [v]
    res = 0

    while len(vert_stack) != len(graph):
        print(vert_stack)
        mini = INF
        ind = -1
        for i in vert_stack:
            for j in range(len(graph[i])):
                if not(j in vert_stack):
                    if graph[i][j] < mini:
                        ind = j
                        mini = graph[i][j]
        vert_stack.append(ind)
        res += mini
    return res


"""
A 0
B 1
C 2
D 3
E 4
F 5
G 6
"""

example1 = [[INF, 5, 10, INF, 2, INF],
         [5, INF, 2, 4, INF, INF],
         [10, 2, INF, 4, INF, 10],
         [INF, 4, 7, INF, 3, INF],
         [2, INF, INF, 3, INF, INF],
         [INF, INF, 10, INF, INF, INF]]

example2 = [[INF, 7, INF, 5, INF, INF, INF],
         [7, INF, 8, 9, 7, INF, INF],
         [INF, 8, INF, INF, 5, INF, INF],
         [5, 9, INF, INF, 15, 6, INF],
         [INF, 7, 5, 15, INF, 8, 9],
         [INF, INF, INF, 6, 8, INF, 11],
         [INF, INF, INF, INF, 9, 11, INF]]

