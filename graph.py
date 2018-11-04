from collections import defaultdict
import json
import datetime

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        # self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def build_graph1():
    with open('bus_stops.json') as f:
        data_nodes = json.load(f)
    with open('bus_routes.json') as f:
        data = json.load(f)

    g = Graph()

    for node in data_nodes:
        g.add_node(node['BusStopCode'])

    for i in range(1, len(data)):
        if data[i]['ServiceNo'] == data[i-1]['ServiceNo'] and data[i]['Direction'] == data[i-1]['Direction']:
            g.add_edge(data[i-1]['BusStopCode'], data[i]['BusStopCode'], abs(data[i-1]['Distance']-data[i]['Distance']))
    return g

def build_graph2():
    g = Graph()

    file = open('roadNet-CA.txt', 'r')
    for line in file:
        pair = line.split()
        g.add_node(pair[0])
        g.add_node(pair[1])
        g.add_edge(pair[0], pair[1], 1)

    return g

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

# g = build_graph1()
# visited, path = dijsktra(g, '83079')
# print(visited)
# print(path)

g = build_graph2()
print("graph finished")
print(datetime.datetime.now())
visited, path = dijsktra(g, '22300')
print(visited)
print(path)
print(datetime.datetime.now())