import json

f = open("busRoutes.json", "r")
data = json.load(f)

adjList = {}
for i in range(100000):
    adjList[i] = []

for service in data:
    for line in data[service]:
        for i in range(len(line) - 1):
            if int(line[i+1]) not in adjList[int(line[i])]:
                adjList[int(line[i])].append(int(line[i+1]))
                # print(int(line[i]), int(line[i+1]))

newAdjList = {}
for stop in adjList:
    if len(adjList[stop]) > 0:
        newAdjList[stop] = adjList[stop]

print(newAdjList)

file = open("busAdjList.json", "w")
json.dump(newAdjList, file)