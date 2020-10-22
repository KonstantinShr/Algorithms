def dfs(v):
    print(v)
    visited[v] = True
    for j in graph[v]:
        if not visited[j]:
            dfs(j)


num_vert = int(input('Enter the number of vertex:'))
graph = []
visited = [False]*num_vert
for i in range(num_vert):
    print("Enter neighbors for vertex #{}".format(str(i)))
    arr_vert = list(map(int, input().split()))
    graph.append(arr_vert)
print("Your graph:\n", graph, "\nThe order of visiting vertices")

dfs(0)
