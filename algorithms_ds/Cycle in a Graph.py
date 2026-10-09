import sys

V = int(input())
graph = []


def correct_i(lis):  # creates int element list with vertex-value = index-value
    corr_lis = []
    for i in lis:
        i = int(i)
        corr_lis.append(i - 1)
    return corr_lis


def correct_num(lis):  # creates str element list with vertex-value = original value
    corr_lis = []
    for num in lis:
        corr_lis.append(str(num + 1))
    return corr_lis


# creating an adjacency list representation
for line in sys.stdin:
    neighbors = []
    neighbors = correct_i(line.split())

    if neighbors[0] == -1:
        graph.append([])

    else:
        neighbors.pop(0)
        graph.append(neighbors)

def dfs(g, start):
    visited = [False] * len(g)
    path = []
    is_cycle = False

    def visit(v):
        nonlocal is_cycle
        nonlocal path
        nonlocal start
        nonlocal visited
        if is_cycle == True:
            return
        path.append(v)
        visited[v] = True
        if g[v] == []:
            path = [start]
        for w in g[v]:
            if w in path:
                path = path[path.index(w):]
                print(len(path))
                print(' '.join(correct_num(path)))
                is_cycle = True
                return
            if not visited[w]:
                visit(w)
        if path != []:
            path.pop()


    visit(start)
    for v in range(len(g)):
        if visited[v] == False:
            start = v
            path = []
            visit(start)
    if is_cycle == False:
        print('neni')


dfs(graph, 0)
