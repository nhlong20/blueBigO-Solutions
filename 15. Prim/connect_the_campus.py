from math import sqrt
from heapq import heappush, heappop
INF = 10**9

def prims(s, graph, visited,  cost):
  n = len(visited)
  cost[s] = 0
  min_heap = [(0,s)]

  while min_heap:
    u = heappop(min_heap)[1]
    visited[u] = True
    for v in range(n):
      if visited[v]: continue
      if cost[v] > graph[u][v]:
        cost[v] = graph[u][v]
        heappush(min_heap, (cost[v], v))
  

def cal_dist(pointA, pointB):
  x1, y1 = pointA
  x2, y2 = pointB
  return sqrt((x1-x2)**2 + (y1-y2)**2)
ans = 0
def solve():
  while True:
    nBuildings = int(input())
    buildings = []
    graph = [[] for _ in range(nBuildings)]
    costs = [INF]*nBuildings
    visited = [False]*nBuildings

    for _ in range(nBuildings):
      x, y = map(int, input().split())
      buildings.append((x,y))


    for i in range(nBuildings):
      for j in range(nBuildings):
        graph[i].append(cal_dist(buildings[i], buildings[j]))

    nCable = int(input())
    for i in range(nCable):
      u, v = map(int, input().split())
      u-=1
      v-=1
      graph[u][v] = 0
      graph[v][u] = 0

    prims(0, graph, visited, costs)

    ans = 0
    for cost in costs: 
      ans += cost
    print("%.2f" % ans)


try:
  solve()
except EOFError:
  exit()
