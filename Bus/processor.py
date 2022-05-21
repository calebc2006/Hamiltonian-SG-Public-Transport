import json

f = open("rawBusRoutes.json", "r")
data = json.load(f)

adjList = {}

for service in data:
    for line in data[service]:
        for i in range(len(line) - 1):
            if line[i] not in adjList:
                adjList[line[i]] = []
            if line[i+1] not in adjList[line[i]]:
                adjList[line[i]].append(line[i+1])

newAdjList = {}
for stop in adjList:
    if len(adjList[stop]) > 0:
        newAdjList[stop] = adjList[stop]

file = open("allStopsAdjList.json", "w")
json.dump(newAdjList, file)