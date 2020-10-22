from collections import deque


def bfs(v):
    visited[v] = True
    queue = deque([v])
    while queue:
        current = queue.popleft()
        visited[current] = True
        print(current)
        for j in graph[current]:
            if not visited[j]:
                queue.append(j)


num_vert = int(input('Enter the number of vertex:'))
graph = []
visited = [False]*num_vert
for i in range(num_vert):
    print("Enter neighbors for vertex #{}".format(str(i)))
    arr_vert = list(map(int, input().split()))
    graph.append(arr_vert)
print("Your graph:\n", graph, "\nThe order of visiting vertices")

bfs(0)
