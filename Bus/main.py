from gettext import find
import json
import heapq
import pandas as pd
import itertools

f = open("Bus/allStopsAdjList.json", "r")
data = json.load(f)
f.close()

targets = [
    "09179",
    "04339",
    "14119",
    "19081",
    "16149",
    "11511",
    "11401"
]
N = len(targets)
allStops = set()


def findAllStops():
    global allStops
    for key in data:
        allStops.add(key)
        for stop in data[key]:
            allStops.add(stop)


def dijkstra(graph, root):  # Graph is an adjList
    dist = {}
    visited = {}
    path = {}
    global allStops
    for stop in allStops:  # Initialise all dist to INF and visited to false
        dist[stop] = 1e9
        visited[stop] = False
        path[stop] = []

    pq = [(0, root)]  # Initialise priority queue of (dist, node)
    dist[root] = 0  # Set dist to root to 0
    path[root].append(root)

    while (len(pq) > 0):
        _, cur = heapq.heappop(pq)
        if visited[cur]:
            continue
        visited[cur] = True

        try:
            for newNode in graph[cur]:
                if dist[cur] + 1 < dist[newNode]:  # If the route through cur is faster, take it!
                    dist[newNode] = dist[cur] + 1
                    path[newNode] = path[cur][:]
                    path[newNode].append(newNode)
                    heapq.heappush(pq, (dist[newNode], newNode))
        except:
            continue

    return dist, path


def generateAdjList():
    adjList = {}
    paths = {}

    for stop in targets:
        adjList[stop] = []
        paths[stop] = {}
        dist, path = dijkstra(data, stop)
        for nextStop in targets:
            adjList[stop].append((nextStop, dist[nextStop]))
            paths[stop][nextStop] = path[nextStop]

    f = open("Bus/targetsAdjList.json", "w")
    json.dump(adjList, f)
    f.close()

    return adjList, paths


def generateAdjMatrix(adjList):
    dfAdjList = {}
    for i in adjList:
        row = adjList[i]
        newRow = []
        for j in row:
            newRow.append(j[1])
        dfAdjList[i] = newRow

    df = pd.DataFrame(dfAdjList, index=targets)
    df.to_csv("Bus/adjMatrix.csv")
    return df


# FINDING SHORTEST LOOP

def printDist(start, end, adjList, paths):
    for stop, dist in adjList[start]:
        if stop == end:
            print(f"\n{start} --> {end}: {dist} stops")
    for stop in paths[start][end]:
        print(stop + " ")


def getDist(start, end, adjList):  # start index -> end index
    for stop, dist in adjList[targets[start]]:
        if stop == targets[end]:
            return dist


def lengthOfCycle(perm, adjList):
    prev = perm[N - 1]
    length = 0
    dists = []

    for i in perm:
        dist = getDist(prev, i, adjList)
        dists.append(dist)
        length += dist
        prev = i

    return length


def generateAllCycles(adjList):
    best = 1e9
    bestPerms = []

    for perm in itertools.permutations(range(N)):
        length = lengthOfCycle(perm, adjList)
        if length < best:
            best = length
            bestPerms = []
            bestPerms.append(perm)
        elif length == best:
            bestPerms.append(perm)

    return best, bestPerms


def printShortestPaths(adjList):
    shortestLength, bestPerms = generateAllCycles(adjList)
    print(
        f"Shortest Length: {shortestLength}\nPaths of length {shortestLength}:")
    for perm in bestPerms:
        path = []
        path = [targets[i] for i in perm]
        path.append(str(targets[perm[0]]))
        print(path)


def printPath(nodes, paths):
    length = 0
    for i in range(len(nodes)-1):
        length += printOnePath(nodes[i].strip(), nodes[i+1].strip(), paths)
    print(f"\nTotal Length: {length} stops")


def printOnePath(a, b, paths):
    for stop in paths[a][b]:
        print(stop, end=', ')
    print("")
    return len(paths[a][b]) - 1


def main():
    findAllStops()
    adjList, paths = generateAdjList()
    matrix = generateAdjMatrix(adjList)

    while True:
        command = input("... ")
        if command == "matrix":
            print(matrix)
            print("")
        if command == "cycles":
            printShortestPaths(adjList)
            print("")
        if command[:4] == "path":
            raw = command[5:]
            nodes = raw[1:-1].split(',')
            for i in range(len(nodes)):
                nodes[i] = nodes[i].strip()[1:-1]
            printPath(nodes, paths)
            print("")
        if command == "help":
            print(
                "Commands are 'matrix', 'cycles', 'path ['', '', '', ...]' and exit")
        if command == "exit":
            return


if __name__ == "__main__":
    main()
