# Advent of Code - http://adventofcode.com/day/9
# From http://adventofcode.com/day/9 
# Typer  : Ginny C Ghezzo 
# Taking the dijkstra algorithm from http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php 
# or 
# http://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python
# What I learned: This is my bad failed code. I could not figure out which \x## evaluated and which did not

import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
else: filename = 'day9data.txt'
file = open(filename,'r')
print(filename)
nodes = []      # names  of the cities (node) TODO: They use a list, why not a set?
distances = {}  # vertex 

def getCities():
    # get the city names and the distances 
    mynodes = []
    mydis = {}
    # TODO : Find the cities not as source 
    for line in file:
        myline = line.rsplit(' ')
        mynodes.append(myline[0])
        mynodes.append(myline[2])
        if myline[0] not in mydis:
            mydis[myline[0]] = {}
        if myline[2] not in mydis:
            mydis[myline[2]] = {}
        mydis[myline[0]][myline[2]] = int(myline[4].rstrip())
    mynodes = list(set(mynodes))
    current = mynodes[0]
    print(mynodes)
    return(mynodes, mydis, current)

nodes, distances, current = getCities()
unvisited = {node: None for node in nodes}        # use None as +inf ?? 
print("unvisited at start: ", unvisited)
visited = {}
currentDistance = 0
unvisited[current] = currentDistance

while True:
    if current not in distances: 
        print('Something wrong with ', current)
    for neighbor, distance in distances[current].items():
        if neighbor not in unvisited: continue 
        newDistance = currentDistance + distance
        if unvisited[neighbor] is None or unvisited[neighbor] > newDistance:
            unvisited[neighbor] = newDistance
    visited[current] = currentDistance
    try: 
        del unvisited[current]
    except: 
        print("What is unvisited when this goes wrong? ", unvisited, " ", current)
    if not unvisited: break 
    candidates = [node for node in unvisited.items() if node[1]]
    try:
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    except IndexError:
        print("error ", current, currentDistance)
    

print(visited)
